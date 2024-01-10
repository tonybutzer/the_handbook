
## WEEK 6 - Case Studies ECO & ET

### Death by Demo

The subjects include:

- cloud activity continues to GROW
    - Dinesh, Trenton
        - next week we will do a STAC/sat-search and xarray using the landsat-pds bucket - PUBLIC, PUBLIC PUBLIC - some buckets are almost Public
    - Mike Oimoen, Logan etc 
    - CHS sponsored science
    - Steffi Kagone working on getting her own CHS Custom space - Just like Neal's
        - Kagone modeled 150 years of Delaware River - now wants to do CONUS.
            - Scientists think big - Science has the answers!
    - Danielson, Postma, Neal et al have Tensorflow experience!
    - Doucette encourages cloud AI/ML and python at EROS.
        - move science into the cloud - I agree obviously
        - Kelcy made the comment that AI/ML is a field where we should share knowledge across projects
    - A CHS Data Lake is needed
    - Tony offers to alpha-test Q-GIS and arcGIS in the cloud. - stay tuned ...
    - Tony frightens Neal with a half-backed cost analyzer Notebook
    - Aaron Friez and Cole K. are planning advanced Pangeo/DASK classes in CHS - using this class as a springboard. - You should attend when it pops up on the calendar,
- phenology - dashboards are nifty.
- machine learning with Tensorflow - what kind of shoe is this?
- evaporation and transpiration for 150 flippin years -- NO SWEAT!
- orchestration - its not just for clarinets and violins - DEFER
- how to cheat at AWS S3 bucketology with import fsspec
- AMAZED at how Many items in this python eco-system boil down to one-line of code.

## Birds-of-a-feather groupings
#### Phenology
[https://afternoon-crag-97068.herokuapp.com/](https://afternoon-crag-97068.herokuapp.com/)
- *Points*
    - python app written in Plotly Dash
    - phenology based on landcover
    - interactive - good responsiveness
    - serverless(CATTLE) - heroku, binder, AWS lambda - AWS Batch(quasi)
- more to come.
    - next week a discussion on HLS - NDVI Dev/Logan/Mike
    - Creating NDVI with Landsat 8 - public data sets and Xarray

[https://www.usgs.gov/core-science-systems/eros/phenology/science/ndvi-foundation-remote-sensing-phenology?qt-science_center_objects=0#qt-science_center_objects](https://www.usgs.gov/core-science-systems/eros/phenology/science/ndvi-foundation-remote-sensing-phenology?qt-science_center_objects=0#qt-science_center_objects)

#### Tensorflow
[http://10.12.68.150:8080/tree/tensorflow-tutorials](http://10.12.68.150:8080/tree/tensorflow-tutorials)
- Run from a container on the mini-pangeo
- Training example shoes and shirts
- The sandal looks like a sneaker to me
- Movie sentiment analysis
- tensorflow for dummies - on kbr - skillport - free free free
- Machine learning research to be actively funded by USGS - Sunne has the contact -
    - Matthew Kuckuk - Reno Nevada

```
/opt/logan/tools/tensorflow$ more Makefile

        docker run -it -p 8080:8888 tensorflow/tensorflow:nightly-jupyter
```


## Case Studies Eco - Data Wrangling

- RAPV2
- HLS
- MRLZ - unzip pipeline

Consider this web app:
[https://rangelands.app](https://rangelands.app)

poor mans version here:
[http://10.12.68.150/user/butzer/tree/opt/logan/00-notebooks/02-eco-viz](http://10.12.68.150/user/butzer/tree/opt/logan/00-notebooks/02-eco-viz)


### Data Pipelines and Orchestration
[etm-conductor-orchestration-v2](https://github.com/tonybutzer/etm/blob/master/02-orchestration-launcher/etm-conductor-orchestration-v2.py)


## Docker Uses

- demo cog generation from sapv2 tif
- demo unzip convert from .img and make cog mrlc-BITv3 
- both of these from custom docker containers and simple docker heuristics

### Viz app for etasw
[http://10.12.68.246/user/butzer/tree/opt/etviz/0-application-et-view](http://10.12.68.246/user/butzer/tree/opt/etviz/0-application-et-view)

[http://10.12.68.246/user/butzer/notebooks/opt/etviz/0-application-et-view/99-vrt-fail.ipynb#](http://10.12.68.246/user/butzer/notebooks/opt/etviz/0-application-et-view/99-vrt-fail.ipynb#)




## Next Week

#### Data Wrangling of MRLC Data
####  Harmonized Landsat and Sentinel HLS
- Cole Krehbiel
- [HLS and geoviews]
    - https://www.google.com/search?client=firefox-b-1-d&q=lp+daac+jupyter+gallery
    - [E-Learning](https://lpdaac.usgs.gov/resources/e-learning/)
    - [Getting Started with Cloud-Native HLS Data in Python](https://lpdaac.usgs.gov/resources/e-learning/getting-started-cloud-native-hls-data-python/)

    - [iowa plotting EVI](https://lpdaac.usgs.gov/resources/e-learning/masking-visualizing-and-plotting-appeears-output-geotiff-time-series-python/)




### From Rich Signell's ocean example
[geoviews example and cog overviews](https://nbviewer.jupyter.org/gist/rsignell-usgs/f4dd62ad1274c5b5ed69e5a6b81c1295)

