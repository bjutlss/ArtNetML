#!/bin/bash
n_gpu=1
cls='vase'
python -m torch.distributed.launch --nproc_per_node=1 train_custom.py --gpu "0" --gpus 1 --local_rank "0"