# HPC Notes

https://www.usgs.gov/center-news/denali-tallgrass-eros-launch-new-era-high-performance-computing-capabilities

https://hpc-aub-users-guide.readthedocs.io/en/latest/octopus/slurm_cheatsheet.html

## Signularity References
- https://sylabs.io/docs/#singularity

- Building containers with Singularity
    - https://www.youtube.com/watch?v=nrgO3Q8-6hQ

- https://singularity.lbl.gov/archive/docs/v2-3/docs-docker

## Useful References

https://hpc-uit.readthedocs.io/en/latest/jobs/interactive.html

https://pangeo.io/setup_guides/hpc.html


https://www.hpc.iastate.edu/guides/containers


https://ioos.github.io/notebooks_demos/other_resources/

https://www.usgs.gov/core-science-systems/sas/arc

https://www.usgs.gov/mission-areas/core-science-systems

https://hpcportal.cr.usgs.gov/hpc-user-docs/jobs/best-practices.html

https://pubs.cray.com/bundle/XC_Series_Programming_Environment_User_Guide_1705_S-2529/page/SLURM_in_Interactive_Mode.html


## Useless References

https://hpcportal.cr.usgs.gov/hpc-user-docs/Resources/training_classes.html

https://www.esma.europa.eu/sites/default/files/library/jc-2018-04_joint_committee_final_report_on_big_data.pdf

https://indico.cern.ch/event/854707/timetable/?view=standard

https://www.tandfonline.com/doi/full/10.1080/17538947.2019.1585976

## Useful Videos

- Slurm Basics
    - https://www.youtube.com/watch?v=49DzPT9HFJM

https://www.google.com/search?client=firefox-b-1-d&q=slurm+for+dummies+youtube+hpc


## Useless Videos



## Ideas

- remote desktop xfce containers etc ... tbd
https://hpc-wiki.info/hpc/Admin_Guide_Fastx

http://xarray.pydata.org/en/stable/examples.html


## Login Nodes and Transfer Nodes


## PANGEO Journey

### Install and Test Miniconda

https://pangeo.io/setup_guides/hpc.html


#### Logon your hpc system now

- tallgrass - my favorite 
- salloc and bash in new run node
- install miniconda


```
mkdir opt/mini
cd opt/minu

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh


conda update conda

```

---



### Signell Help

Follow this recipe and let me know if it works for you: https://discourse.holoviz.org/t/setting-up-working-environment-for-tutorial/1794/4

### from conda env base

```
cd /home/butzer/opt/etscrum/2_ET_HPC/signell



conda config --add channels conda-forge --force
source activate base
conda install mamba -y
mamba env create -f pangeo_env.yml

```

