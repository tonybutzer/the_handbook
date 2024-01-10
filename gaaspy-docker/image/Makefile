cat:
	cat Makefile


Image=tbutzer/gaaspy-docker

build:
	docker build -t ${Image} .


run:
	docker run -it ${Image} bash


conda:
	conda config --add channels conda-forge --force
	conda install -y mamba
	mamba env create -f environment.yml
	#mamba install `cat requirements.txt`
