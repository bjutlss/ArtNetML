# FFB6D
This is an unofficial source code and a modified version of **FFB6D: A Full Flow Biderectional Fusion Network for 6D Pose Estimation**. ([Arxiv](https://arxiv.org/abs/2103.02242), [Video_Bilibili](https://www.bilibili.com/video/BV1YU4y1a7Kp?from=search&seid=8306279574921937158), [Video_YouTube](https://www.youtube.com/watch?v=SSi2TnyD6Is))


```
@InProceedings{He_2021_CVPR,
author = {He, Yisheng and Huang, Haibin and Fan, Haoqiang and Chen, Qifeng and Sun, Jian},
title = {FFB6D: A Full Flow Bidirectional Fusion Network for 6D Pose Estimation},
booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
month = {June},
year = {2021}
}

@InProceedings{He_2020_CVPR,
author = {He, Yisheng and Sun, Wei and Huang, Haibin and Liu, Jianran and Fan, Haoqiang and Sun, Jian},
title = {PVN3D: A Deep Point-Wise 3D Keypoints Voting Network for 6DoF Pose Estimation},
booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
month = {June},
year = {2020}
}
```

## Installation
- Install CUDA 10.1 / 10.2
- Set up python3 environment from requirement.txt:
  ```shell
  pip3 install -r requirement.txt 
  ```
- Install [apex](https://github.com/NVIDIA/apex):
  ```shell
  git clone https://github.com/NVIDIA/apex
  cd apex
  export TORCH_CUDA_ARCH_LIST="6.0;6.1;6.2;7.0;7.5"  # set the target architecture manually, suggested in issue https://github.com/NVIDIA/apex/issues/605#issuecomment-554453001
  pip3 install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
  cd ..
  ```
- Install [normalSpeed](https://github.com/hfutcgncas/normalSpeed), a fast and light-weight normal map estimator:
  ```shell
  git clone https://github.com/hfutcgncas/normalSpeed.git
  cd normalSpeed/normalSpeed
  python3 setup.py install --user
  cd ..
  ```
- Install tkinter through ``sudo apt install python3-tk``

- Compile [RandLA-Net](https://github.com/qiqihaer/RandLA-Net-pytorch) operators:
  ```shell
  cd ffb6d/models/RandLA/
  sh compile_op.sh
  ```

For more Information please see the official source code!
