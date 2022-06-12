#!/bin/bash
cls='vase'
tst_mdl=train_log/custom/checkpoints/vase/FFB6D_vase_best.pth.tar
python3 -m demo -dataset custom -checkpoint $tst_mdl -cls $cls -show
