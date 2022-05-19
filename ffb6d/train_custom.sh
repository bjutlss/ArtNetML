#!/bin/bash
n_gpu=4
cls='vase'
python -m torch.distributed.launch --nproc_per_node=$n_gpu train_custom.py --gpus=$n_gpu --cls=$cls