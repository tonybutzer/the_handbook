# Tensorflow in mini-pangeo ECO Sandbox

## Scientists
- Pat Danielson
- Kory Postma

## Test Case
- NLCD tensorflow ML training
- use Tesnorflow

## Objectives
- demonstrate the ease of running this via jupyter and the cloud
- allows for sharing ideas and code and data in cloud based science
- fulfills one of Doucette's goals for AI/ML in the cloud  



## shrub.yml - from Kory

```
#conda env create -f shrub.yml
##conda activate shrub
##pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org tensorflow
##To upgrade tensorflow run this command twice
##pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org tensorflow --upgrade
name: shrub
channels:
  - conda-forge
  - defaults
dependencies:
  - python
  - pydensecrf #for CRF algorithm (segmentation post-processing)
  - cython #needed for compiling pydensecrf
  - numpy #needed for numerical calculations on cpu
  - Pillow #needed for image operations
  - scikit-learn #ML algos and utilities
  - matplotlib ##plots
  - seaborn ##make matplotlib plots nicer!
  - ipython #optional - for running code in ipython
  - jupyter #for accessing and executing jupyter notebooks
  - pandas  #data wrangling
  #cannot install tensorflow and gdal at the same time
  #- tensorflow=2.1 #-gpu  #for deep learning
  - gdal #OSGeo GDAL
  - tqdm #Progress Bar
  #to install packages not available in conda
  - pip
```
