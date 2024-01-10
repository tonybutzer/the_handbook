from continuumio/miniconda3

SHELL ["/bin/bash", "--login", "-c"]

run apt-get update && apt-get install -y make

copy ./ /home/

workdir /home

run conda config --add channels conda-forge --force && \
    conda install -y mamba && \
    mamba env update -n base --file environment.yml

# run make conda && conda info | grep -i 'base environment'

#RUN /bin/bash -c "source activate gaass_i2i"

# SHELL ["/bin/bash"]

# ENV PATH /opt/conda/envs/gaass_i2i/bin:$PATH
# run conda activate gaass_i2i

#run source /opt/conda/etc/profile.d/conda.sh && conda activate gaass_i2i


run python dependent.py

