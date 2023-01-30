# Face Modelling
Using generative models to generate high quality face embeddings

## Setup
1. `conda env update -f environment.yml`
1. `conda activate faces`
1. `pre-commit install`
1. `poetry update && poetry install`

## Plan

1. Use a very fast face detector which runs on cpu - MTCNN, Faceboxes, DeepFace has in-built alignment
1. Align faces - Possibly DeepFace, or [MediaPipe](https://google.github.io/mediapipe/solutions/face_mesh.html#face-transform-module)
1. Embed faces - unsupervised pretraining
1. Remove anomalies - Use DBScan for clustering, include some non-face clusters. Remove embeddings that are in non-face cluster.
1. Index embeddings

## Helpful Links
- https://towardsdatascience.com/face-recognition-on-330-million-images-at-400-images-per-second-b85e594eab66
- https://github.com/davidsandberg/facenet
- https://github.com/zisianw/FaceBoxes.PyTorch
- https://susanqq.github.io/UTKFace/
- https://github.com/timesler/facenet-pytorch
- http://vis-www.cs.umass.edu/fddb/
- http://vis-www.cs.umass.edu/lfw/
- https://github.com/1adrianb/face-alignment
- https://google.github.io/mediapipe/solutions/face_mesh.html#face-transform-module
- https://github.com/1adrianb/unsupervised-face-representation
- SWaV https://arxiv.org/pdf/2006.09882.pdf
- https://www.adrianbulat.com/downloads/ECCV2022/face_representation_learning.pdf
- https://dl.acm.org/doi/pdf/10.1145/3347447.3356752?accessTab=true
- https://google.github.io/mediapipe/solutions/face_detection
- BlazeFace - https://arxiv.org/pdf/1907.05047.pdf