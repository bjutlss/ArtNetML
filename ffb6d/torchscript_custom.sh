#!/bin/bash
n_gpu=1
cls='vase'
tst_mdl=train_log/linemod/checkpoints/${cls}/FFB6D_${cls}_best.pth.tar
torchrun --nproc_per_node=1 train_custom.py --gpu "0" --gpus 1 -script_net -checkpoint $tst_mdl