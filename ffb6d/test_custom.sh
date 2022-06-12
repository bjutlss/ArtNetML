#!/bin/bash

cls='vase'
tst_mdl="./train_log/custom/checkpoints/vase/FFB6D_vase_best.pth.tar"
python3 -m torch.distributed.launch --nproc_per_node=1 train_custom.py --gpu '0' --cls $cls -eval_net -checkpoint $tst_mdl -test -test_pose # -debug

