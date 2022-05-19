#!/bin/bash

n_gpu=2
cls='vase'
python -m torch.distributed.launch --master_port 33330 --nproc_per_node=$n_gpu train_custom.py --gpus=$n_gpu --cls=$cls