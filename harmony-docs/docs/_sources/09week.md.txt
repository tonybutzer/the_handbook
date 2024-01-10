# WEEK 9 Docker Week - lightning talk EDITED

## Faking it with docker
- what if we built a docker image and launched a bunch of containers?
- will that scale?

## BUILDING An aws pricing docker image
- tbutzer/aws-price
- python app
- github 
    - [code link](https://github.com/tonybutzer/harmony/tree/main/class/01-docker-container-class/app-aws-price/code)
    - [https://github.com/tonybutzer/harmony/tree/main/class/01-docker-container-class/app-aws-price/code](https://github.com/tonybutzer/harmony/tree/main/class/01-docker-container-class/app-aws-price/code)

### Today I am going to jump on a bunch of systems
- what do they have in common?
    - they all run docker!
- what can I do with docker?
    - anything you could do with linux
        - only better, faster, cheaper and stronger
- where are you going to jump around
    - local windows box - with cygwin fake linux
    - local linux server in sioux falls
    - on-prem EROS linux systems in computer room 2
    - in the AWS cloud in oregon
        - in the Landsat - virtual-private-cloud - account
        - in the Invasive - VPC (logan and neal's space)
        - soon in my new lcmap AWS CHS space - if jeff briden says ok

### Dockerfiles and Makefiles - i repeat myself

## Freedom of Religion - Infrastructure Agnostic

| Account | Location | OS | Scaling | Application |
| ---- | ---- | ---- | ---- | --- |
| LCMAP | AWS Custom | Linux | Docker, k8s | lcmap |
| Landsat | AWS Big | Linux | all | Collection-2 |
| Invasive | AWS Custom | Linux | TBD | Cheatgrass |
| WaterSmart | Not Yet :-( | Linux| Docker | ET |
| LandFire | Not Yet :-( | Linux| Docker | Fire stuff |
| pangeo.chs | AWS CHS Cloud | Jupyter Linux| DASK | Training |
| LSRD | llsrlscd04, on-prem | Linux | Docker, VM | Development|


## Data at our Fingertips in the cloud 
### A short informal list

| Curator | Catalog | Collection | Assets | Format | POC |
| ---- | ---- | ---- | ---- | --- | --- |
| EROS | STAC 0.7 | C2 utm and albers | bands, metadata | COG | N. Roberts
| LPDAAC | cmrSTAC | HLS v1.5 | bands, metadata | COG | A. Friesz
| (AWS) Joe Flasher | STAC | sentinel-2 | bands, resolution, repeat | COG | Aussies |
| Flasher,Planet | STAC | Landsat-8 TOA | bands, pilot | COG | Tony |
| Flasher,ESA | STAC | sentinel-2 | bands, resolution, repeat | jpeg2000(yuck) | ESA |


### Demo this Tony
`ubuntu@ip-10-12-69-233:/opt/harmony/class/01-docker-container-class/`

- essh logan
    - docker run -it --rm tbutzer/aws-price python3 awsprice.py njp



### Go thru the Teams Chat - for ET Mosaics
- jose website review docker used to run sphinx and nginx
    - ls /etc/ | grep release
- llsrlscd04 - aws cli - apt-get update - apt-get install dc
    - bash - host llsrlscd04
    - cd opt/docker/aws cli 
        - aws s3 ls dev-et-data --no-sign     # anonymous

```
for i in {1..40}; do echo $i ; host 152.61.84.$i; done
```


### Detailed Docker Training available from Tony and others - Ron Dilley etc



[https://nbviewer.jupyter.org/github/tonybutzer/harmony/blob/main/class/01-docker-container-class/docker-tony-tutorial-aws-onboard.ipynb](https://nbviewer.jupyter.org/github/tonybutzer/harmony/blob/main/class/01-docker-container-class/docker-tony-tutorial-aws-onboard.ipynb)




## From Medium Article Guest Notebook

[https://github.com/shakasom/zonalstatistics](https://github.com/shakasom/zonalstatistics)

[https://github.com/shakasom/zonalstatistics/blob/master/Zonal_Statistics_Sentinel.ipynb](https://github.com/shakasom/zonalstatistics/blob/master/Zonal_Statistics_Sentinel.ipynb)



---
## END of Week 9
---
