# WEEK 8 - Remote Sensing is Hard

- Making it easy will challenge us
- We will need naive ambition and energy to conquer this

## How will we ever make science easy
1. Move data - all data into shared data lakes - prewrangled - WIP
2. Move the Scientist to the data
3. Build an easy ito use software eco-system/set-of-libraries in python
4. Teach the scientists just enuf python
5. Teach the library builders and devops people lots of python and the details of remotely sensed data
6. Build middleware that deals with all the nuances of Remote Sensed Data
    - Open Data Cube ?
7. Understand the trade-offs and adapt our thinking accordingly
8. Communicate like crazy - Collaborate like the human race depends on it
9. Buy water futures over California on the NASDAQ

## TL;DR - Evangelize and Implement the Pangeo Vision

## Intro Paragraph
> for next tuesdays class - I am working on a simplified waubay example using landsat-8 only from a mature catalog as well as more explanations on pandas, xarray, and STAC catalogs - we will have some AI plans and composite plans in Git that I will glide thru as well ... more to come. lots of training and practical examples are emerging ... some data wrangling for Steffi as well


## Purpose of the WEEK8 Class

- More examples of notebooks building xarrays
    - wuabay without all of the sat-api in your face
    - how cloudy is it - Maine?
    - Albers is alright, UTM is alright 'They just seem a little weird', 'surrender, surrender' - 4326
    - using lite-stac - little cube - open data cube lite - limited utility
        - smaller memory AOI's only - works with 4326 AOI and UTM data
        - ad-hoc science - quick demos
        - heavier science likely needs 
            - open data cube
            - or something like lcmaps interface via ChipMunk, aardvark - http ... # perhaps sped up
            - we will play (R&D) with open data cube and sentinel - over Maine - and deal with projections
- Gentle introduction into Open Data Cube abtractions and middleware
- Visualize and verify Steffi's new input data for full CONUS Models
- Identify the R&D cloud efforts and try to tie them together into a theme
    - Invasive
    - AI tensorflow - meets NLCD - Rangelands
    - Geomedian, Euclidean Composites as base inputs to land classifiers
    - 4 jupyter/pangeo(mini) sandboxes - 2 in landsat (need to go away) 1 in science(invasive) a few(4) in the queue and bigPangeo
- 50 greatest western movies - into a pandas data frame - how do folks manage streaming decision fatigue
- pandas and xarray and geopandas - have similar slicing methods - raster and vector spaces
- Initial glimpse into the challanges of compositing
- Projections hurt my brain - Albers, UTM and 4326
- one on one or small splinter sessions on cloud meets python meets - data - meets scientist are happening - 
- Emerging, nascent data inputs - landsat[utm,albers], sentinel, - climate, soils, etc ...
    - `spreadsheet` - show it now?


## Coming Soon

- more data wrangling of Cheatgrass - unzipping pipeline ... cflux AGAIN - `Logan?`
- HLS trials and tribulations - Devandra?
    - Opportunities to work with the LPDAAC ['Cole K.', 'Aaron F.']
- ... AI .. tensorflow ... into git ....
- composite NLDC Rangeland Pat, Brett, Kory
    - compare/collaborate Aussie composite methods with US EROS methods - develop best-of-breed
    - young github repo exists here
        - [https://github.com/tonybutzer/composite/tree/main/10-code-reference](https://github.com/tonybutzer/composite/tree/main/10-code-reference)

> The World Geodetic System (WGS) is a standard for use in cartography, geodesy, and satellite navigation including GPS. This standard includes the definition of the coordinate system's fundamental and derived constants, the ellipsoidal (normal) Earth Gravitational Model (EGM), a description of the associated World Magnetic Model (WMM), and a current list of local datum transformations.

> The latest revision is WGS 84 (also known as WGS 1984, EPSG:4326), established and maintained by the United States National Geospatial-Intelligence Agency since 1984, and last revised in 2004

## Overview

- git
- data to be organized properly in the cloud
    - Collection-2 STAC and sat-search improvements
    - Albers with STAC and sat-search
- data we are playing with
    - landsat-pds - Landsat 8 public data set - sponsored by Planet and AWS
- HLS (BOF) birds-of-a-feather working group
    - Need to have Cole K go thru his notebook and what he knows - Aaron Friez as well

---
[https://earthdata.nasa.gov/esds/harmonized-landsat-sentinel-2](https://earthdata.nasa.gov/esds/harmonized-landsat-sentinel-2)

[https://svs.gsfc.nasa.gov/4745](https://svs.gsfc.nasa.gov/4745)

[https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4880&button=recent](https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4880&button=recent)

## info and viz
- repeat cycle - revisits
- covid-sats

![](http://www.beyondgeek.com/wp-content/uploads/2013/02/Sputnik_670.jpg)

## STAC Catalog - high level collections
[http://10.12.69.233/user/butzer/notebooks/opt/notebook/00-Harmony/01-composites-Albers-new/00-list-STAC-Catalog-Collections.ipynb](http://10.12.69.233/user/butzer/notebooks/opt/notebook/00-Harmony/01-composites-Albers-new/00-list-STAC-Catalog-Collections.ipynb)

## Simplifed Waubay

    - uses sat-search
    - Dinesh this is a good way to play with moving the AOI

[http://10.12.69.233/user/butzer/notebooks/opt/notebook/00-Harmony/00-A-waubay-simple/0-waubay-simple-via-open-data-cube-lite.ipynb](http://10.12.69.233/user/butzer/notebooks/opt/notebook/00-Harmony/00-A-waubay-simple/0-waubay-simple-via-open-data-cube-lite.ipynb)


## Git Repo Tour

- tensorflow
- composite
    - [THE GRID](https://www.usgs.gov/media/images/conterminous-us-landsat-analysis-ready-data-ard-tiles)
    - [https://www.usgs.gov/core-science-systems/nli/landsat/landsat-shapefiles-and-kml-files](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-shapefiles-and-kml-files)


## Netflix Distration 20
http://10.12.69.233/user/butzer/notebooks/opt/notebook/00-Harmony/01-composites-Albers-new/00-list-STAC-Catalog-Collections.ipynb

## Validating Input Data via YML Config
    - Pandas

[https://nbviewer.jupyter.org/github/tonybutzer/etviz/blob/master/0-0-10-degree-viz/99-yaml-input-pandas.ipynb](https://nbviewer.jupyter.org/github/tonybutzer/etviz/blob/master/0-0-10-degree-viz/99-yaml-input-pandas.ipynb)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/600px-Pandas_logo.svg.png)


---
## [https://registry.opendata.aws/sentinel-2-l2a-cogs/](https://registry.opendata.aws/sentinel-2-l2a-cogs/)

---

## END OF WEEK8
---

## Future Classes
### Docker
### STAC, sat-api, sat-search  --> curators, end-points, catalogs, items, assets ... more json than you can stand
### Data Transfer to the Denali ... ??? ??? ???
