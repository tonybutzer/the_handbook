rm -fr /home/ubuntu/miniconda3/envs/ouch
conda config --add channels conda-forge --force
source activate base
conda install mamba -y
mamba env create -f pangeo_env.yml
#(cd ~/opt/cubelib; make build)

