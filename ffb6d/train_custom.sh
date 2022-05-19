#!/bin/bash
n_gpu=8
cls='vase'
torchrun --nproc_per_node=$n_gpu train_custom.py --gpus=$n_gpu --cls=$cls