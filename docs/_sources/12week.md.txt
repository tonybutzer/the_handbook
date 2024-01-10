---
# Week 12

## Summary

- `Kelcy's notebook` -- Landsat Collection-2 and STAC
- `HLS` Notebooks for mosaic overlap issue
    - start with browse for less clouds and more coverage
    - Look for these NASA LPDAAC concepts in today's notebooks
        - CMR - Common Metdata Repository
        - UMM -- Unified Metadata Model
        - Authentication
- DAGs
- Data Wrangling
- Road to Reusable Code - How?
    - Start with common goals
        - Open Source Python
        - In the cloud
            - and in the HPC(s)
    - Use the same platform for sharing
        - Jupyter Notebooks
        - github and code.usgs.gov 
    - Refine and Refactor your Code so people want to reuse it
        - Self documented or well documented
        - Clean Code -- eliminate code smells
        - Make your code so simple people want to use it
            - good examples
                - xarray
                - hvplot
                - folium
                - pandas
        - Use opinionated approaches
            - xarray, pandas, geopandas - all reinforce rigor and reusability
    - good reusable code allows for lots of work done in few lines of code
    - good code is always a journey
    - Organize Science by common interests in addition to projects
        - Promote non-silo Communication
    - make it simple to install - advertise it

## Future Classes
- Model Analysis work Olena Boiko is working on for evapo
    - We will showcase these notebooks in a future class

### Direct S3 or portal or something in between
- STAC Assets
    - http (portal like)
    - s3://
    - gdal virtual filesystem specifiers /vsicurl/ -- /vsis3/
    - Kelcy and Nathan - map the http to s3 for collection2

---

### Some Folks Just Cannot Let Go of Portals https://landsatlook.usgs.gov/data

```
def convert_llurl(ll_url: str) -> str:
    """
    Convert a landsat look url to an S3 url
    """
    return ll_url.replace('https://landsatlook.usgs.gov/data', 's3://usgs-landsat')

def open_dateset(ll_url: str):
    """
    Open a file with gdal
    """
    with rasterio.open(convert_llurl(ll_url)) as f:
        return f
#     return gdal.Open(path, gdal.ReadOnly)---
```

---

## Kelcy Notebook


[https://code.usgs.gov/klsmith/pangeo-examples/-/blob/master/lcmap-time-series-ccd.ipynb](https://code.usgs.gov/klsmith/pangeo-examples/-/blob/master/lcmap-time-series-ccd.ipynb)


---

---


#### Nathan's less obvious method to cheat http by using s3

```
# remove 33 characters and replace them
#remove everything forward of /collection from the cloudfront object URL
greens = pd.DataFrame(greens['Green'].str[33:])
swirs = pd.DataFrame(swirs['Swirs'].str[33:])
#append s3://usgs-landsat to the front of the URLs
greens = pd.DataFrame("s3://usgs-landsat"+greens['Green'])
swirs = pd.DataFrame("s3://usgs-landsat"+swirs['Swirs'])
```

- kelcy's code is more readable IMHO


---
#### Sentinel COG Example

### Sentinel STAC gets this preference for direct S3 access correct

```
"href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/19/T/CJ/2020/10/S2A_19TCJ_20201014_0_L2A/B02.tif",
```

```
ubuntu@ip-10-12-69-188:~$ aws s3 ls sentinel-cogs
                           PRE sentinel-s2-l2a-cogs/
ubuntu@ip-10-12-69-188:~$ aws s3 ls sentinel-cogs/sentinel-s2-l2a-cogs/
                           PRE 1/
                           PRE 10/
                           PRE 11/
                            ...
```


#### HLS Example
- Buckets
    - lp-prod-protected
    - lp-prod-public

```
import rasterio as rio
e='https://lpdaac.earthdata.nasa.gov/lp-prod-protected/HLSS30.015/HLS.S30.T18TYR.2020278T154121.v1.5.B04.tif'
b04 = rio.open(e)

#dir(b09)
b04.shape


'href': 'https://lpdaac.earthdata.nasa.gov/lp-prod-public/HLSS30.015/HLS.S30.T19TCM.2020278T154121.v1.5.jpg'
```

[https://cmr.earthdata.nasa.gov/search/concepts/G1969487860-LPCLOUD.umm_json](https://cmr.earthdata.nasa.gov/search/concepts/G1969487860-LPCLOUD.umm_json)
```
"https://lpdaac.earthdata.nasa.gov/s3credentials"

Description:    "api endpoint to retrieve temporary credentials valid for same-region direct s3 access"
```

---
## Everyone is moving to the cloud -- getting there is ________

- Opening new horizons:
    - EU
    - How to migrate the Copernicus Global Land Service to a Cloud environment

- conversion of space-based Earth Observation information into `actionable` knowledge 
- Moving Global Land Services to another completely new and technological challenging cloud computing environment is `not a trivial job.`
- providing `clear suggestions` for an efficient ‘cloudification’ of the Copernicus global land production lines and user interfaces, 

- Benefits
    - greater transparency and reproducibility of the data processing chains, enhancing trust
    - better scalability to handle the large volume of data we expect from future satellites
    - better integration with downstream processing chains and thus more value delivered to research and industry

---

```
--- 
Group: "HLS Interest Group"
HLS: 
  - 
    ECO: 
      - "Sujan Parajuli"
      - "Devandra Dahal"
      - "Logan Megard"
      - "Neal Pastick"
      - "Mike Oimoen"
    LCMAP: 
      - "Kelcy Smith"
    LPDAAC: 
      - "Cole Krehbiel"
      - "Aaron Friesz"
    PANGEO: 
      - "Tony Butzer"
    VegDyn: 
      - "Dinesh Shrestha"
      - "Trenton Benedict"
```


## Class Recap

- Still attacking data wrangling
- people should get friendly with github/gitlab -- code.usgs.gov
- pangeo.chs.usgs.gov and other subsidized infrastructure platforms

### References

#### If the Mask fits .. understand it
[https://rasterio.readthedocs.io/en/latest/topics/masks.html](https://rasterio.readthedocs.io/en/latest/topics/masks.html)

### Nice Tutorials - Guest Teacher of the Week

- [https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/landsat-in-Python/](https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/landsat-in-Python/)
- Pat Danielson - volunteer

## Projections and Geoviews
[https://geoviews.org/user_guide/Projections.html](https://geoviews.org/user_guide/Projections.html)

- Managing Overlap in Albers 
- pangeo demos
- github albers-mosiac repo
    - https://github.com/tonybutzer/albers-mosaic



## What's Happening in Pangeo Land

- ECO team will continue to get high speed data access to HLS
    - we have just scratched the surface on how to scale
    - looking for an open source, xarray perhaps, solution to mosiacing like ARCMAP
        - needs to handle overlapping scenes intelligently
- Scotty H - has lots of great tutorials - a little over my head - but i'm learning.
- DataLake 
    - interim - s3://dev-et-data/data-lake - can access it from pangeo.cr.usgs.gov
    - Now that Kristi Kline is on the case we may get more attention on a USGS cloud S3 based Data Lake.
- Binder is pretty cool - more free pangeo compute - 
- The scientist is the critical resource on the planet - never compute


## Direct acyclic Graphs

- used in DASK
- used in python code graphing/flow charting - dependency trees
- graphviz and pyan3 # python analyzer
    - [https://graphviz.org/](https://graphviz.org/)
- consists of vertices and edges (also called arcs), with each edge directed from one vertex to another, such that following those directions will never form a closed loop.

![dag](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Tred-G.svg/440px-Tred-G.svg.png)

## Data Wrangling Working Group

## Data Lake Work

- Class A Data Assets
    - Landsat Collection-2
    - Sentinel Cogs
    - Harmonized Landsat Sentinel (1.5)

- Class B Data Assets
    - NLCD
    - LCMAP Products

- Class C Data Assets
    - Soil ...

Concepts:
   - shared data - makes less wrangling
   - shared python code - allows reuse
   - cross-project communication - breaks silos and diverse teams build better solutions
   - data deluge is coming - lets be ready to filter and use what we want
        
        
    
# Signell Reading List

- https://github.com/pangeo-data/cog-best-practices
- https://github.com/intake/intake-stac/tree/main/examples    

## Other

- https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/landsat-in-Python/
        

---

### Pangeo Startup Sequence

![pang](./Assets/pangeo-k8s-startup-event-log.PNG)


---

---
## Denali integration Scenarios

- composite on AWS --- Characterize on Denali or Tallgrass
- Water Evaporation and Runoff on AWS --- Evaluate Water Balance Model fidelity on Denali using Stream Guage Data

    - brand new USGS `Landsat Collection2` - Surface Reflectance in UTM
        - coming soon Albers
    - Experimental `Harmonized Landsat-Sentinel`
    - nearFuture Suomi NPP will carry five science instruments 
        - Suomi NPP is the first satellite mission to address the challenge of acquiring a wide range of land, ocean, and atmospheric measurements 
- Synergies with google maps and geojson.io
- NO LICENSE FEES
- Jen Rover is in HPC school
- Should be able to use notebooks in both environments - cloud and HPC
    - IF the python `version monster` does not get you!

---

## END OF WEEK 12

---
