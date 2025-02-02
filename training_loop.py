import time

import jax
from flax.training.common_utils import shard

from monitoring import get_wandb_log_step_lambda
from batch import setup_dataloader
from dataset import setup_dataset
from repository import save_to_local_directory
from training_step import get_training_step_lambda


def get_training_state_params_from_devices(params):
    return jax.device_get(jax.tree_util.tree_map(lambda x: x[0], params))


def training_loop(
    text_encoder,
    text_encoder_params,
    vae,
    vae_params,
    unet,
    state,
    rng,
    max_train_steps,
    num_train_epochs,
    train_batch_size,
    output_dir,
    log_wandb,
    get_validation_predictions,
    num_devices,
):

    # rng setup
    train_rngs = jax.random.split(rng, num_devices)

    # dataset setup
    train_dataset = setup_dataset(max_train_steps)
    print("dataset loaded...")

    # batch setup
    total_train_batch_size = train_batch_size * num_devices
    train_dataloader = setup_dataloader(train_dataset, total_train_batch_size)
    print("dataloader setup...")

    # Create parallel version of the train step
    training_step_lambda = get_training_step_lambda(text_encoder, text_encoder_params, vae, vae_params, unet)
    jax_pmap_train_step = jax.pmap(
        fun=training_step_lambda,
        axis_name="batch",
        donate_argnums=(1,2,),
    )
    print("training step compiling...")

    milestone_step_count = min(10_000, max_train_steps)
    print(f"milestone step count: {milestone_step_count}")

    wandb_log_step = get_wandb_log_step_lambda(
        get_validation_predictions,
    )

    # Epoch setup
    t0 = time.monotonic()
    global_training_steps = 0
    global_walltime = time.monotonic()
    for epoch in range(num_train_epochs):

        for batch in train_dataloader:
            batch_walltime = time.monotonic()

            batch = shard(batch)

            state, train_rngs, train_metrics = jax_pmap_train_step(
                batch, train_rngs, state, 
            )

            global_training_steps += num_devices

            is_milestone = (
                True if global_training_steps % milestone_step_count == 0 else False
            )

            if log_wandb:
                # TODO: is this correct? was only unreplicated before, with no averaging
                global_walltime = time.monotonic() - t0
                delta_time = time.monotonic() - batch_walltime
                wandb_log_step(
                    global_walltime,
                    global_training_steps,
                    delta_time,
                    epoch,
                    train_metrics,
                    state.params,
                    is_milestone,
                )

            if is_milestone:
                save_to_local_directory(
                    f"{ output_dir }/{ str(global_training_steps).zfill(12) }",
                    unet,
                    get_training_state_params_from_devices(state.params),
                )
