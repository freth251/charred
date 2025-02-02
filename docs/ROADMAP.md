# CHARRED Roadmap

## Use cases

OCR
Statistical reconstitution of damaged textual artifacts. (inpainting to predict the missing caracters, ex MARI)


## Dataset

DONE: Integrate LAION-HR: https://huggingface.co/datasets/laion/laion-high-resolution
Integrate WiT dataset: https://huggingface.co/datasets/google/wit
Augment all datasets to match ByT5's C4 training language distribution: https://huggingface.co/datasets/allenai/c4 https://huggingface.co/datasets/mc4
Integrate synthetic HTML/SVG/CSS graphic/layout/typography dataset
Integrate document layout segmentation and understanding dataset
Integrate calligraphy dataset
Integrate grapheme-in-the-wild dataset
Filter out samples with a low-aesthetic image score or a meaningless caption https://github.com/google-research/google-research/tree/master/vila https://github.com/google-research/google-research/tree/master/musiq https://github.com/christophschuhmann/improved-aesthetic-predictor https://www.mdpi.com/2313-433X/9/2/30 https://paperswithcode.com/dataset/aesthetic-visual-analysis https://www.tandfonline.com/doi/full/10.1080/09540091.2022.2147902 https://github.com/bcmi/Awesome-Aesthetic-Evaluation-and-Cropping https://github.com/rmokady/CLIP_prefix_caption https://github.com/google-research-datasets/Image-Caption-Quality-Dataset https://github.com/gchhablani/multilingual-image-captioning https://ai.googleblog.com/2022/10/crossmodal-3600-multilingual-reference.html https://www.cl.uni-heidelberg.de/statnlpgroup/wikicaps/ https://huggingface.co/docs/transformers/main/tasks/image_captioning https://www.mdpi.com/2076-3417/13/4/2446 https://arxiv.org/abs/2201.12723 https://laion.ai/blog/laion-aesthetics/ 

Cache freezed models (ByT5 and VAE) embeddings
Save preprocessed images and original datasets in JPEG XL
Preprocess images with JAX-native methods: https://jax.readthedocs.io/en/latest/jax.image.html https://dm-pix.readthedocs.io/ https://github.com/4rtemi5/imax https://github.com/rolandgvc/flaxvision

## Codebase

https://github.com/deepmind/chex
https://github.com/mpi4jax/mpi4jax
https://github.com/jeremiecoullon/jax-tqdm

## Training

DONE: Implement JAX/FLAX SD 2.1 training pipeline with ByT5-Base instead of CLIP: https://github.com/patil-suraj/stable-diffusion-jax https://github.com/huggingface/diffusers/blob/main/examples/text_to_image/train_text_to_image_flax.py https://huggingface.co/google/byt5-base https://huggingface.co/blog/stable_diffusion_jax
DONE: WandB monitoring
OpenTelemetry monitoring including JAX profiler tracing artifact uploading
Implement Mini-SNR loss rebalancing: https://arxiv.org/abs/2303.09556
Implement on-the-fly validation: https://huggingface.co/docs/diffusers/en/conceptual/evaluation
Integrate Big Vision optimizaitions: https://github.com/google-research/big_vision
Use ByT5-Large instead of ByT5-Base: https://huggingface.co/google/byt5-large
Implement streaming, mini-batching and gradient accumulation with image aspect ratio and tokenized caption size bucketing: https://github.com/NovelAI/novelai-aspect-ratio-bucketing https://optax.readthedocs.io/en/latest/gradient_accumulation.html https://optax.readthedocs.io/en/latest/api.html#optax.MultiSteps
Use ByT5-XXL instead of ByT5-Large: https://huggingface.co/google/byt5-xxl https://github.com/google-research/t5x/blob/main/docs/models.md#byt5-checkpoints https://github.com/google-research/t5x/blob/main/t5x/scripts/convert_tf_checkpoint.py
Port to JAX and Integrate Imagen, SDXL and Deep Floyd improvements: https://github.com/lucidrains/imagen-pytorch https://github.com/deep-floyd/IF https://stable-diffusion-art.com/sdxl-beta/ https://huggingface.co/docs/diffusers/api/pipelines/if https://huggingface.co/spaces/DeepFloyd/IF https://huggingface.co/DeepFloyd/IF-I-XL-v1.0 https://huggingface.co/DeepFloyd/IF-II-L-v1.0 https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler https://huggingface.co/DeepFloyd/IF-notebooks/tree/main https://huggingface.co/blog/if https://huggingface.co/docs/diffusers/main/en/api/pipelines/if https://stability.ai/blog/deepfloyd-if-text-to-image-model https://deepfloyd.ai/ https://www.assemblyai.com/blog/how-imagen-actually-works/ https://www.youtube.com/watch?v=af6WPqvzjjk https://www.youtube.com/watch?v=xqDeAz0U-R4
Save checkpoints using JAX-native methods: https://flax.readthedocs.io/en/latest/api_reference/flax.training.html https://flax.readthedocs.io/en/latest/guides/use_checkpointing.html#save-checkpoints


## Inference

DONE: Implement JAX/FLAX text-to-image inference pipeline with ByT5-Base instead of CLIP: https://huggingface.co/docs/diffusers/training/text2image https://github.com/patil-suraj/stable-diffusion-jax
Production AOT with IREE over Java JNI/JNA/Panama: https://github.com/openxla/iree https://github.com/iree-org/iree-jax https://jax.readthedocs.io/en/latest/aot.html https://jax.readthedocs.io/en/latest/_autosummary/jax.make_jaxpr.html https://jax.readthedocs.io/en/latest/_autosummary/jax.xla_computation.html https://github.com/openxla/stablehlo https://github.com/openxla/xla https://github.com/openxla/openxla-pjrt-plugin https://github.com/iml130/iree-template-cpp
Load checkpoints using JAX-native methods https://flax.readthedocs.io/en/latest/guides/use_checkpointing.html#id1
Implement OCR and Document understanging inference pipeline with ByT5 text decoder
Implement text encoding CPU offloading with int8 precision
Implement accelerated U-Net prediction and VAE decoding with int8 precision : https://github.com/TimDettmers/bitsandbytes https://huggingface.co/blog/hf-bitsandbytes-integration

## Exploration

https://github.com/google-research/google-research/tree/master/vrdu
https://github.com/google-research/google-research/tree/master/wt5 https://github.com/google-research/google-research/tree/master/invariant_explanations
https://github.com/google-research/google-research/tree/master/ul2 https://ai.googleblog.com/2022/10/ul2-20b-open-source-unified-language.html
https://github.com/google-research/t5x/blob/main/t5x/train.py
https://github.com/google-research/t5x/blob/main/docs/usage/finetune.md
https://github.com/google-research/text-to-text-transfer-transformer/blob/main/t5/data/tasks.py
https://github.com/google-research/text-to-text-transfer-transformer/blob/main/t5/data/mixtures.py
https://github.com/google-research/t5x/blob/main/docs/usage/eval.md
https://github.com/google-research/t5x/blob/main/docs/usage/infer-seqio.md
https://github.com/google-research/t5x/blob/main/t5x/contrib/gpu/t5/configs/runs/finetune.gin
https://github.com/google-research/t5x/blob/main/t5x/contrib/gpu/t5/configs/runs/finetune_mnli.gin
https://github.com/google-research/t5x/blob/main/t5x/contrib/gpu/t5/configs/runs/finetune_squad1.gin
https://github.com/google-research/t5x/blob/main/t5x/configs/runs/finetune.gin
https://github.com/google-research/t5x/tree/main/t5x/examples/scalable_t5
https://github.com/google-research/t5x/tree/main/t5x/contrib/moe
https://github.com/tensorflow/mesh/blob/master/mesh_tensorflow/transformer/moe.py
https://arxiv.org/abs/2101.03961
https://www.infoq.com/news/2021/02/google-trillion-parameter-ai/
https://towardsdatascience.com/understanding-googles-switch-transformer-904b8bf29f66
https://towardsdatascience.com/the-switch-transformer-59f3854c7050
https://github.com/google-research/longt5
https://arxiv.org/abs/2208.02813
https://github.com/google-research/google-research/tree/master/moe_models_implicit_bias
https://github.com/google-research/google-research/tree/master/moe_mtl
https://github.com/google-research/google-research/tree/master/dselect_k_moe
https://huggingface.co/google/switch-c-2048
https://github.com/google-research/t5x/tree/main/t5x/contrib/calm
https://github.com/google-research/google-research/tree/master/pali
https://laion.ai/blog/paella/
https://laion.ai/blog/open-flamingo/
https://laion.ai/blog/datacomp/
https://aclanthology.org/2022.semeval-1.226/
https://medium.com/nlplanet/a-full-guide-to-finetuning-t5-for-text2text-and-building-a-demo-with-streamlit-c72009631887
https://github.com/gsarti/t5-flax-gcp
https://github.com/PiotrNawrot/nanoT5
https://github.com/Ki6an/fastT5
https://www.marktechpost.com/2023/02/06/google-ai-open-sources-flan-t5-a-transformer-based-language-model-that-uses-a-text-to-text-approach-for-nlp-tasks/
https://arxiv.org/abs/2203.17189
https://github.com/google-research/t5x/tree/main/t5x/contrib/gpu/scripts_gpu
https://huggingface.co/dbmdz/t5-base-conll03-english
https://huggingface.co/mesolitica/finetune-dependency-t5-base-standard-bahasa-cased
https://huggingface.co/datasets/wikiann
https://huggingface.co/datasets/xtreme
https://huggingface.co/datasets/joelito/lextreme
https://huggingface.co/datasets/polyglot_ner
https://huggingface.co/datasets/xglue
https://huggingface.co/datasets/euronews
https://huggingface.co/datasets/Babelscape/wikineural
https://huggingface.co/datasets/Babelscape/multinerd
https://huggingface.co/datasets/tner/multinerd
https://huggingface.co/datasets/tner/wikineural
https://huggingface.co/datasets/universal_dependencies
https://surfacesyntacticud.github.io/
https://multiconer.github.io/
https://multiconer.github.io/multiconer_1/
https://registry.opendata.aws/multiconer/
https://registry.opendata.aws/fast-ai-nlp/
https://registry.opendata.aws/lowcontext-ner-gaz/
https://registry.opendata.aws/code-mixed-ner/
https://registry.opendata.aws/lei/
https://huggingface.co/datasets/MultiCoNER/multiconer_v2
https://arxiv.org/abs/2208.14536
https://github.com/Alibaba-NLP/KB-NER https://github.com/modelscope/AdaSeq
https://github.com/mckysse/gain
https://github.com/SairamNaragoni/named-entity-recognition-T5
https://github.com/MarSanTeam/Complex_NER_SemEval
https://huggingface.co/docs/transformers/tasks/token_classification
Simple T5 NER example: https://colab.research.google.com/drive/1obr78FY_cBmWY5ODViCmzdY6O1KB65Vc