#!/bin/bash

n_gpu=2
cls='vase'
torchrun --nproc_per_node=$n_gpu train_lm.py --gpus=$n_gpu --cls=$cls