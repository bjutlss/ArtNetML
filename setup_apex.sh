git clone https://github.com/NVIDIA/apex
cd apex
export TORCH_CUDA_ARCH_LIST="8.0,8.6,"  # set the target architecture manually, suggested in issue https://github.com/NVIDIA/apex/issues/605#issuecomment-554453001
pip3 install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ..

git clone https://github.com/hfutcgncas/normalSpeed.git
cd normalSpeed/normalSpeed
python3 setup.py install --user
cd ..

cd ffb6d/models/RandLA/
sh compile_op.sh