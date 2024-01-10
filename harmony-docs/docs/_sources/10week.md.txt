# Week 10 - We are Really on to Something Here:

---
![](http://ontheworldmap.com/usa/state/maine/map-of-maine.jpg)


---

### A lot to cover today

- Remember: - Tony does topical small sessions on specific topics as part of the Pangeo/Open Data Cube outreach project

---
---

- synergies between the cloud and hpc
- high speed data movement
- Remote Sensing Catalogs of pixels at our service
    - `Sentinel` L2A
    - old Landsat 8 TOA
    - brand new USGS `Landsat Collection2` - Surface Reflectance in UTM
        - coming soon Albers
    - Experimental `Harmonized Landsat-Sentinel`
    - nearFuture Suomi NPP will carry five science instruments 
        - Suomi NPP is the first satellite mission to address the challenge of acquiring a wide range of land, ocean, and atmospheric measurements 
- Synergies with google maps and geojson.io
- NO LICENSE FEES
- A support group and a PANGEO community with really smart people to cheat off
- A talented pool of folks from SD Universities - pride
- Scientists with noble missions - wonderful!
- We can write `our own apps` that do just what we want them to do!
- get rid of WINDOWS and all of its poor engineering.
- tell Claudia - we can and do run PANGEO/jupyter on Denali and Tallgrass

---
[UTM Link svg](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system#/media/File:Universal_Transverse_Mercator_zones.svg)

# Introducing Self-Directed Labs
- more to come ...


### Tony yamls on 
- http://www.yamllint.com/
- https://jsonlint.com/

## Next 2 classes - Yaml
```
Today: '2-16-2021'
  Theme: 'Sentinel Data Exploration and Discovery'
  Title: 'Cloud Based Sentinel CogS'
  Sensor: 'Sentinel'
  Data_Tier: 'L2A'
  Projection: 'UTM'
  Science_Application: 'Compositing'
  Sandbox: 'pangeo.chs.usgs.gov'
  Status: 'Exploration early R&D'
  Purpose: 'Class Example'
  AWS_Document: 'https://registry.opendata.aws/sentinel-2-l2a-cogs/'
  AOI: 'Maine'
  City: 'Augusta'
  Subtopics: ['Browse', 'Tiles', 'Clouds', 'Geojson', 'Google_Maps']
  Git_Repo_Ref: 'https://github.com/tonybutzer/composite/tree/main/00-notebooks/00-wip-geojson-viewer'
```

  

## Future Classes

- Pangeo Objects - STAC - Xarray
- Map Projections - warp speed
    - geopandas intersections - operations- 
        - new_gdf = gdf.loc[gdf.within(atlanta_shapely)]
        - new_gdf = gdf.loc[gdf.intersects(atlanta_shapely)]
- Compositing using cloud assets
- Water model evaluation on Denali with stream guage integration and using PANGEO - open source!
- Managing python packages in the evolving Pangeo opinionated ecosystem
    - docker, conda, pip -- "GDAL" -- "GDAL"
    - Do not pip install gdal, do not install GDAL inside a virtual-env. Instead, use Conda.
---
![](Assets/pip-install-meme.PNG)

## The DEMOs
- lets begin

```
https://pangeo.chs.usgs.gov/user/butzer@contractor.usgs.gov/notebooks/opt/composite/00-notebooks/00-wip-geojson-viewer/98-cloud-zealot-short-list.ipynb

--- 
Alias: jovyan
Mission: "Help Bill Gates save the planet with better technology"
Notebook: "https://pangeo.chs.usgs.gov/user/butzer@contractor.usgs.gov/notebooks/opt/composite/00-notebooks/00-wip-geojson-viewer/98-cloud-zealot-short-list.ipynb"
Partners: 
  - AWS
  - ESA
  - "Pangeo Community"
Purpose: "Build advocacy for the cloud and image processing"
Sandbox: pangeo.chs.usgs.gov
Title: "Cloud Zealot Engagement Strategy"
User: jupyter-pangeo
What: "tl;dr: it’s a play on jovian which means a Jupiter-like planet"
Python_Packages:
  - pandas
```

## Message from Woods Hole Oceanographic Institute

---
[6:42 AM] `Signell, Richard P`
---
Tony, thanks for the update!   I have been wondering about how things were going!  I'm excited we have an updated environment now at pangeo.chs.usgs.gov with the latest async capabilities for xarray/fsspec/zarr that make many things much faster. 


### Demo 2 - flip thru aoi's i have shown off - waubay, rumira 

http://www.yamllint.com/

```
--- 
Notebook: 00-geojson-viewer-panel.ipynb
Purpose: "Improve understanding of cool panel widget apps"
Python_Packages: 
  - panel
  - folium
  - json
  - geojson
Sandbox: pangeo.chs.usgs.gov
User: butzer@contractor.usgs.gov
github: composite
path: opt/composite00-notebooks/00-wip-geojson-viewer
prototype: "For Danielsons - Auto Composite/Animator and Dwyer Cube Tool"
```

### Demo 3 clouds and coverage and browse images - 

- free pangeo
- cheap chromebook
- free sentinel - cloud COGs

### Science its like magic only real!
- Did you know Geographers smile way more than ordinary folks.

```
--- 
Notebook: 10-less-clouds-display-thumbnails-jpg-maine-with-sentinel
Purpose: "Gentle intro to Sentinel Assets (COGs) in us-west-2"
Python_Packages: 
  - geopandas
  - folium
  - geojson
  - satsearch
  - intake
  
Sandbox: pangeo.chs.usgs.gov
User: butzer@contractor.usgs.gov
github: composite
path: opt/composite00-notebooks/00-wip-geojson-viewer
Opinion: "Clouds - who needs them"
```


```
DETAILS
{'datetime': '2020-05-02T15:50:34Z',
 'platform': 'sentinel-2b',
 'constellation': 'sentinel-2',
 'instruments': ['msi'],
 'gsd': 10,
 'data_coverage': 39.35,
 'view:off_nadir': 0,
 'eo:cloud_cover': 0.84,
 'proj:epsg': 32619,
 'sentinel:latitude_band': 'T',
 'sentinel:grid_square': 'DK',
 'sentinel:sequence': '0',
 'sentinel:product_id': 'S2B_MSIL2A_20200502T153809_N0214_R011_T19TDK_20200502T194632',
 'created': '2020-09-18T23:16:32.727Z',
 'updated': '2020-09-18T23:16:32.727Z',
 'sentinel:valid_cloud_cover': True,
 'sentinel:utm_zone': 19,
 'sentinel:data_coverage': 39.35}


more ...

B02:
              eo:bands:
              - center_wavelength: 0.4966
                common_name: blue
                full_width_half_max: 0.098
                name: B02
              gsd: 10
              roles:
              - data
              title: Band 2 (blue)
              type: image/tiff; application=geotiff; profile=cloud-optimized
```
---


---

## Everyone loves a Grid

---
![hls](./Assets/hls-grid-conus.PNG)

---

![a](https://dragon3.esa.int/documents/247904/266366/Sentinel-2-MSI_Product_Types_Figure_1_v3/262f604c-de1e-4cf7-b4f6-abdd7f0dc5fd?t=1523262257162)
https://earth-info.nga.mil/GandG/update/index.php?action=home#tab_coord-data

![](https://earth-info.nga.mil/GandG/update/img/MGRS_1km_Polygon_Shapefiles_Coverage.jpg)

https://www.usgs.gov/centers/eros/science/usgs-eros-archive-sentinel-2?qt-science_center_objects=0#qt-science_center_objects

- The Sentinel-2 tiling grid is referenced to the U.S. Military Grid Reference System (MGRS). 
- Tiles can be fully or `partially` covered by image data. 
    - Partially covered tiles correspond to those at the edge of the swath.


### Demo - klm - shapefiles - geoviews - maps

```
--- 
Notebook: 00-sentinel-klm-study
Purpose: "geometry vector intersection example"
AOI: "Maine and tiles"
Python_Packages: 
  - geopandas
  - shapely
  - feona
  
Sandbox: pangeo.chs.usgs.gov
User: butzer@contractor.usgs.gov
github: composite
path: opt/composite00-notebooks/00-wip-geojson-viewer
Opinion: "geoviews base * maine layers cool - zoom them"

COOL_FEATURES:
  - prune by geometric intesection operation with state of maine
  - save as geojson --> geojson.io
  - save as klm --> maps    https://www.google.com/maps/d/home
```

### Demo geojson.io - reads geopandas - intersecting with maine

- Why did you work so hard in jupyter tony
- file: Downloads: maine_s2_tiles.json

[geojson pop up](http://geojson.io/#map=7/44.840/-72.762)



## Google Maps - this is Soooooo COOOOL - COOL KOOL KLM noice
[map](https://www.google.com/maps/d/edit?mid=18I407FsgH_r1yYjnPMUprXVkWkZFSIpk&usp=sharing)

## END OF WEEK10

---
