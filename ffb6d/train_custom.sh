#!/bin/bash


torchrun --nproc_per_node=1 train_custom.py --gpu "0" --gpus 1 --opt_level=O1 --cls="vase"
