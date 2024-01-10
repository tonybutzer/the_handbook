
hi:
	echo hi tony
	cat Makefile

conda:
	echo do a conda deactivate before running this
	conda config --add channels conda-forge
	# conda install -y mamba
	mamba env create

nuke:
	rm -fr /data2/butzer/miniconda3/envs/Landsat_1

validate:
	python3 validate_landsat.py

start:
	./start_jupyter_notebook.sh
