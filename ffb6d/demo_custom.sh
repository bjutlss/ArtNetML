#!/bin/bash
cls='vase'
tst_mdl=train_log/custom/checkpoints/${cls}/FFB6D_${cls}_best.pth.tar
python3 -m demo -dataset custom -checkpoint $tst_mdl -cls $cls -show
