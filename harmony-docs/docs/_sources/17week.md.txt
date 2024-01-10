# Week 17 Google Cloud and AWS Oh My

- so many technical options and choices - so little time.

## What does this class teach again?

1. How to exploit the AWS Cloud via CHS
2. PANGEO - Xarray, Pandas, Holoviews ...
3. DevOps for the science guys
4. Moving, Wrangling Data with less effort and less time
4. Don't MOVE your data - teleport to Oregon - us-west-2
5. Jupyter and Python - easy to write - easy to run
6. Docker its in there

## Future Classes
1. Logan - HLS experiments for ECO-invasive
2. Aaron - s3 direct access LPDAAC HLS
3. Kelcy - time series landsat
4. Pat Danielson, Kory, Brett, Brian Tolk -- Compositing - NLCD and FireScience
5. Simson --> Jupyter Quick Start
6. Erica Degagga --> Landfire Initiatives in the Cloud
7. Tony --> Searching disorganized git repos
8. Neal CoP presentation on using Cloud + Cloud + HPC + AI/ML/DL


## Past Videos

- teams does not make it easy to share for new users
    - past channel is not available
    - test with Simson negative result

- Game of Thrones is 67 hours -- this is less than 20 so far

### K 90daytemp

- k:/90daytemp/butzer/AWS_PANGEO_VIDEOS 

#### Featured Video
K:\90daytemp\butzer\AWS_PANGEO_VIDEOS\2020_12_08_AWS_PANGEO On-boarding with Tony and Neal.mp4


## Pangeo Access

- https://taskmgr.chs.usgs.gov/servicedesk/customer/portal/10/create/251
- https://taskmgr.chs.usgs.gov/servicedesk/customer/portal/10



### Evapo Cartoon
[https://github.com/tonybutzer/et/blob/master/docs/source/00status.md](https://github.com/tonybutzer/et/blob/master/docs/source/00status.md)

- https://github.com/tonybutzer/et/blob/master/docs/source/00status.md

## Class Context

1. Projects that use mutiple modern compute resources
2. CHS AWS development accounts - EC2 elastic, ephemeral computer -- with S3 and git for persistence
3. HPC - especially Tallgrass - cause its availabkle and has GPUs
4. Part of our model family SSEBop is computed/modeled using Google Cloud Platform and GEE
5. GSUTIL and RCLONE featured
6. Refresher on DOCKER and SINGULARITY
7. using pangeo.chs.usgs.gov for displaying ssebop
8. Open Data Cube abstractions BUT with PANGEO for Landsat Albers Scenes

## Demo Overview

1. Look at google cloud bucket assets - ssebop
2. demo how to replicate/sync/copy those to our AWS DataLake
3. demo using docker to build an image for gsutil -- google utility
4. demo running the container on AWS
5. demo running the container/sif on Tallgrass
6. demo looking at the tif file with Pangeo on tallgrass via ssh tunnel of port 8888

---
1. redo Nate's Waubay for albers and rgb
    - composite repo?

- https://console.cloud.google.com/storage/browser/ssebop-modis/Annual
## Rclone Examples

- tony --> umyssh minipangeo

```
 1984  cat Dockerfile
 1985  cat Makefile
 1986  cd
 1987  ls
 1988  rclone config
 1989  ls
 1990  rclone listremotes
 1991  rclone config
 1992  rlone ls sbop:/ssebop-modis/
 1993  rclone ls sbop:/ssebop-modis/
 1994  rclone sync -P sbop:/ssebop-modis/Annual et-data:/dev-et-data/datalake/ssebop-modis/Annual/
 1995  aws s3 ls dev-et-data/datalake/ssebop-modis/Annual/
 1996  aws s3 ls dev-et-data/datalake/ssebop-modis/Annual/ --human
 1997  gdalinfo /vsis3/dev-et-data/datalake/ssebop-modis/Annual/y2003_modisSSEBopETv4_actual_mm.tif
 1998  ls
 1999  ls -l
 2000  rclone listremotes
 2001  rclone ls sbop:/ssebop-modis
 2002  rclone ls sbop:/ssebop-modis --help
 2003  rclone lsjson sbop:/ssebop-modis
 2004  rclone lsjson sbop:/ssebop-modis/Annual
 2005  rclone ls sbop:/ssebop-modis/Annual
 2006  history
```

## ARCPY vs. Open Source


## Databases are so yesterday

## But if you insist on postgres
### I am talking to you OpenDataCube

- THEN - at least use docker to minimize the PAIN!

```
ubuntu@ip-10-12-68-246:/opt/cube-in-a-box$ more docker-compose.yml
version: '3'

services:
  postgres:
    image: postgis/postgis:10-2.5
    environment:
      - POSTGRES_DB=opendatacube
      - POSTGRES_PASSWORD=opendatacubepassword
      - POSTGRES_USER=opendatacube
    ports:
      - 5432:5432
    restart: always

  jupyter:
    build: .
    environment:
      - DB_HOSTNAME=postgres
      - DB_USERNAME=opendatacube
      - DB_PASSWORD=opendatacubepassword
      - DB_DATABASE=opendatacube
      - AWS_NO_SIGN_REQUEST=true
      - STAC_API_URL=https://earth-search.aws.element84.com/v0/
    ports:
      - "8080:8888"
    volumes:
      - ./notebooks:/notebooks
    restart: always
    command: jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='secretpassword'
```

## What does a world class data center look like?

1. lean and agile
2. Highly TRAINED
3. communicates across informal channels
4. Common Goal - effective use of the planet's limited resources - 
5. A world or universe view
6. fosters the right CULTURE
    - sharing and confidence
    - respects each other's expertise
    - has each other's back
    - has fun at work
    - rejects management styles that don't inspire

## These classes propose PANGEO as a way for science
- Open Data Cube - is an instance of PANGEO
    - its database for me represents a barrier to entry
    - that said its a cool and powerful abstraction for building xarray timeseries applications that run in Pangeos
