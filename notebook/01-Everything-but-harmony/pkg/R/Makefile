echo:
	echo hi from R builder


git:
	(cd /opt/notebook ; make)


r-apt:
	sudo apt-get update
	sudo apt-get install -y --no-install-recommends \
		fonts-dejavu \
    		unixodbc \
    		unixodbc-dev \
    		r-cran-rodbc \
    		gfortran \
    		gcc 

r-conda:
	sudo -E conda config --add channels conda-forge
	sudo -E conda install --quiet --yes \
    	'r-base=3.6.1' \
    	'r-caret=6.0*' \
    	'r-crayon=1.3*' \
    	'r-devtools=2.0*' \
    	'r-forecast=8.7*' \
    	'r-hexbin=1.27*' \
    	'r-htmltools=0.3*' \
    	'r-htmlwidgets=1.3*' \
    	'r-irkernel=1.0*' \
    	'r-nycflights13=1.0*' \
    	'r-plyr=1.8*' \
    	'r-randomforest=4.6*' \
    	'r-rcurl=1.95*' \
    	'r-reshape2=1.4*' \
    	'r-rmarkdown=1.14*' \
    	'r-rodbc=1.3*' \
    	'r-rsqlite=2.1*' \
    	'r-shiny=1.3*' \
    	'r-sparklyr=1.0*' \
    	'r-tidyverse=1.2*' \
    	'unixodbc=2.3.*'
	sudo -E conda clean --all -f -y 
	# sudo -E fix-permissions ${CONDA_DIR}
	sudo -E conda install --quiet --yes r-e1071
