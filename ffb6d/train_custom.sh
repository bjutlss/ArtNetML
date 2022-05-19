#!/bin/bash

n_gpu=2
cls='vase'
python -m torch.distributed.launch --master_port 66660 --nproc_per_node=$n_gpu train_lm.py --gpus=$n_gpu --cls=$cls