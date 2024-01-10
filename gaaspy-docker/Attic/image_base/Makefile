cat:
	cat Makefile


Image=tbutzer/gaaspy-docker-a

build:
	docker build -t ${Image} .


run:
	docker run -it ${Image} bash

runv:
	docker run -it -v `pwd`:/home ${Image} bash


mamba:
	conda config --add channels conda-forge --force
	conda install -y mamba
	mamba env create -f environment.yml
	#mamba install `cat requirements.txt`

conda:
	conda config --add channels conda-forge --force
	conda install --file requirements.txt
	#mamba env create -f environment.yml
	#mamba install `cat requirements.txt`
