conda create --name ffb6d python=3.6
conda activate ffb6d
conda install -c menpo opencv3
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
conda install mamba
cat requirements.txt | xargs -n 1 mamba install