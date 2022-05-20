#!/bin/bash
n_gpu=1
cls='vase'
python -m torch.distributed.launch --nproc_per_node=1 train_lm.py --gpu "0" --gpus 1