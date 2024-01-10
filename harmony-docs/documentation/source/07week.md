
## WEEK 7

## Overview

1. Focus on Public Data 
2. Demo of S3, STAC and Collection 2 in pangeo.chs.usgs.gov
3. Repeat Demo of S3 from the mini-pangeo - with animations
    - Dinesh, Trenton and Pat Danielson - used this for self-directed study
4. Talk about class-project synergies
5. Adjourn

## Nathan Roberts Collection-2 at your Fingertips

- Nathans role at EROS
- Other Training Opportunities
- Synergies with the LPDAAC Trainers
- Past Pangeo Courses and Future Plans
- Nathan's Masters Thesis with and without Cloud based Landsat



## THE DEMO

- https://www.usgs.gov/center-news/eros-releases-collection-2-boosting-cloud-access-accuracy-value-landsat-archive?qt-news_science_products=1#qt-news_science_products
[LINK](https://www.usgs.gov/center-news/eros-releases-collection-2-boosting-cloud-access-accuracy-value-landsat-archive?qt-news_science_products=1#qt-news_science_products)

> Director Loria said the movement to cloud processing and cloud data access reflects a significant paradigm shift for the USGS and DOI with regard to how Landsat data products will be accessed and used for science research and applications.

> Collection 2 offers cloud access to Landsat’s nearly 50-year record of Earth surface conditions, alongside a host of improvements to data quality and easier access to Level-2 data products.

- Collection2 - 5 weeks total - 450,000 scenes/day
- Collection1 - 18 Months total -- 25,000 scenes each day

> As a result of those efforts, the release of Collection 2 on December 1, 2020 will mark a new era for users of Landsat data. Collection 2 also features improved geodetic and geometric accuracy across the archive using the European Space Agency (ESA) Ground Reference Image, which will bolster efforts to harmonize Landsat data and data collected by Europe’s Copernicus Sentinel-2 satellites. The Landsat Level-2 products—surface temperature and surface reflectance—from 1984 through the present are also available without special requests, offering instant access to Landsat geophysical science products that will power energy balance or urban heat island studies as application examples.


- https://prd-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/atoms/files/LSDS-1388-Landsat-Cloud-Optimized-GeoTIFF_DFCB-v2.0.pdf


# Take it away Nathan


## Tony leverages Nathan's work for Class
### Demos

## Class-Project Synergies
1. All hands - all of these projects are connected in this class
    - Landfire
    - LCMAP
    - NLCD
    - Evapotranspiration
    - Invasive Species - Cheatgrass
    - Fews - geoserver/geoengine
2. Composites
    - We should pilot some of this work using Open Data Cube examples as a starting point.
    - NLCD
    - Brett Bunde interest


## Public Data Most Notable

1. Landsat-8 PDS - Development Data - Proof of Concept
2. Landsat Collection-2 ARD CARD4L - soon to replace the above data - for real science
3. Sentinel data and now in COGS vs. JPEG2000 format
4. Harmonized Landsat and Sentinel - version 1.5
    - Logan and Devandra - exploring this now.


## Sentinel 2 Public Data

### I FOUND SOME SENTINEL-2 COGS!!!!!!
- more to come on public data access via STAC

- https://registry.opendata.aws/sentinel-2-l2a-cogs/

- https://registry.opendata.aws/

- https://registry.opendata.aws/sentinel-2/


## AWS S3 Pricing

There are three major costs associated with S3:

- Storage cost: charged per GB / month. ~ $0.03 / GB / month, charged hourly
- API cost for operation of files: ~$0.005 / 10000 read requests, write requests are 10 times more expensive
- `Data transfer outside of AWS region:` ~$0.02 / GB to different AWS region, ~$0.06 / GB to the internet.

Based on volume and region the actual prices differs a bit, but optimization techniques stay the same. I will use the above prices in following cost estimates.


## Open Data Cube Advertisement

#### Abstractions make science simpler

- Using Jupyter and python will increase international cooperation for EROS
- In global change science we cannot be xenophobic
    - Rejoining Paris Climate Agreement - 197 countries

> Rarely is there consensus among nearly all nations on a single topic. But with the Paris Agreement, leaders from around the world collectively agreed that climate change is driven by human behavior, that it’s a threat to the environment and all of humanity, and that global action is needed to stop it. It also created a clear framework for all countries to make emissions reduction commitments and strengthen those actions over time. 

[cube-in-a-box sentinel-2 example](https://github.com/opendatacube/cube-in-a-box/blob/2a6fd9c34a2ea2e24a124548ac359092d4082d11/notebooks/Sentinel_2.ipynb)

---

## END OF Week7
---

---

## Harmony Cookbook

## Modeling in AWS
### Data Pipelines and Orchestration


## Docker


```
---

---

```
FROM developmentseed/geolambda:full
WORKDIR /home/geolambda
```




2. WEEK whenever - Delaware River Basin AOI
	- https://panel.holoviz.org/reference/widgets/FileDownload.html

## More Resources - to be sorted
https://code.chs.usgs.gov/pangeo/notebooks/landsat/-/tree/master/Advanced%20Tutorial

https://code.chs.usgs.gov/pangeo/notebooks

## Final Projects
https://earth-env-data-science.github.io/projects.html

## Rich Signell Influence, Experience and Why Cloud

https://medium.com/pangeo/cloud-performant-netcdf4-hdf5-with-zarr-fsspec-and-intake-3d3a3e7cb935

Tony, I discovered something by Accident today.   If you add use "panel" as your urlpath in binder, it displays all your notebooks with Panel as apps.    Check out the last binder link here: 
https://github.com/reproducible-notebooks/Holoviz-Demos#holoviz-demos

[Yesterday 4:22 PM] Signell, Richard P
    Ooh this is cool too!    https://edu.oggm.org/en/latest/explorer.html

[Yesterday 12:44 PM] Signell, Richard P
    Tony, check out Ryan's book! https://earth-env-data-science.github.io/intro
​[Yesterday 12:44 PM] Signell, Richard P
    It's not really a book.   It's actually a course.  He describes how he "onboards" folks to Pangeo (essentially)
Edited​[Yesterday 12:44 PM] Signell, Richard P
    Look at the menu on the left 
​[Yesterday 12:45 PM] Signell, Richard P
    And then look at the Capstone project list: https://earth-env-data-science.github.io/projects.html
​[Yesterday 12:47 PM] Signell, Richard P
    This came up in the discussion here: https://github.com/pangeo-data/jupyter-earth/issues/11#issuecomment-740059579
A curated list of learning resources  · Issue #11 · pangeo-data/jupyter-earthFollowing up from the EarthCube meeting on Sept 10, one item that came to light was that it would be valuable to have a curated / opinionated list of learning resources to onboard scientists to the...github.com​[Yesterday 12:47 PM] Butzer, Tony (Contractor)
    that sounds perfect - this 2nd mouse approach feels nice
​[Yesterday 12:47 PM] Signell, Richard P
    I love that the students all did projects using the tools and have binder links!
​[Yesterday 12:48 PM] Butzer, Tony (Contractor)
    Neal Pastick is already a pangeo zealot - got is aws space today!
​[Yesterday 12:48 PM] Butzer, Tony (Contractor)
    we will be talking to neal - you will be a consultant on our data wrangling pipeline
​[Yesterday 12:53 PM] Signell, Richard P
    Sounds good!



2. LAB
3. Organizing our DATA Inputs in the Cloud
	- Fundamentals of S3
	- S3 is an object store
		- mostly not a big deal - but sometimes ...
	- Data Wrangling
	- Slow Data Transfers
		- ssh and scp
	- VPN do's and dont's 
3. LAB

---

## Project Initiation, Kickoff, and Approach

- Jump in with both feet approach.
- Gabriel Senay, Steffi Kagone - trail blazers
- Neal Pastick as trail blazer
- Continuous Training - Train The trainer
    - Example Steffi and Gabe Parish now writing visualizations directly

## Cloud Immersion Concept

### Use the cloud for EVERYTHING
- website
- kanban
- jupyter hub  - mini-pangeos
- all your data storage
    - move from clunky Netapps and archaic windows storage architectures
- leverage others work
- collaborate like hell

## Why

### For selfish reasons

- Impress your friends
- looks nice on the resume
- its more fun
- you don't have to deal with people you don't like

### Headlines

- Netflix Delivers Billions of Hours of Content Globally by Running on AWS 
- Steffi Kagone does 150 days of work in just THREE!

### Procurement delays not applicable

### Scalability

### USGS/DOI Efficiencies
- Remember DCOI threats
- Remember Cloud First
- Used to be mandates as a top down push
- Now science customer pull
- cost efficiencies
- It is irresponsible not to use the cloud

### Open Source Advantages
- numerous articles on why open source

### Python Momentum

### My favorite - less data wrangling - MORE SCIENCE

