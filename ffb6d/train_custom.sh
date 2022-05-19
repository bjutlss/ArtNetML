#!/bin/bash
n_gpu=8
cls='vase'
python -m torch.distributed.launch --nproc_per_node=$n_gpu train_custom.py --master_port 6660 --gpus=$n_gpu --cls=$cls