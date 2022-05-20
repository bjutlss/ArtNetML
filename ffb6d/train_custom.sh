#!/bin/bash
n_gpu=8
cls='vase'
python3 -m torch.distributed.launch --nproc_per_node=$n_gpu train_custom.py --gpus=$n_gpu --cls=$cls