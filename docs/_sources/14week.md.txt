# Week 14 - Olena -- matplotlib and pandas

## Overview

1. Introduction - Tony
2. Evapo model evaluation landscape - `Stefanie Kagone`
3. Using Xarray slicing and Pandas to automate Spreadsheet Model Analysis - `Olena Boiko`
4. Apply cloud solutions to HLS plipelines - `Logan Megard`
5. Using Open Data Cube to align pixels and then bigPangeo (netcdf ingest) to look at clouds in the cloud - tony

---
# EROS Items of Interest

1. Science continues to elevate
    - Pete Doucette  - Data Center Director
    - Terry Sohl - Science Lead
2. Aaron Friez (Pangeo/DAAC/Science - Workshop/Lecture)
    - Organized -- April 5?
3. Cali - searching for an intern
    - In charge of collating disparate/disaggregated training
    - "Oh Cali" - "if the world could just be aggregated"
4. Summer Hours for AWS Onboarding - begin May 1. - 
    - Get Vaccinated - save a scientist we need them.
5. Evapo - seeks partnership with Jim Rowland on project cloud account similar to Neal's and Kelcy's
6. Evapo Actrivities
    - Next cloud model please - SSeBop - meets Modis meets cloud - Thanks Claudia, Olena and Steffi
    - Co-sponsor for NLCD data wrangling and emerging datalake prototype.
        - Dinesh and Trenton to test NLCD data lake and HLS access
    - HUC12 - zonal stats - impress your stakeholder with a map-reduced spreadsheet
        - Data starts to inform as information
7. HLS Activities Logan
    - Tony still does not like Authentication nuances
    - Rehearsing wrangling for Devandra and Sujan
8. Open Data Cube - cube-in-a-box - (now a word from my sponsor)
    - higher level abstraction - hint at what is possible. - black box - black magic approach.
    - Hey ODC don't make me index and learn Postgresql and PostGIS - my life is already disaggregated enough
9. Tony wakes up and uses github.io
    - Using the cloud == FAIL!
    - Using Tony's home server == FAIL
    - USING GITHUB.IO - I found Goldilocks - this one is just right!

## Favorite/Featured References

- http://gallery.pangeo.io/repos/pangeo-data/landsat-8-tutorial-gallery/landsat8.html
- https://docs.dea.ga.gov.au/notebooks/Frequently_used_code/Masking_data.html

### Pangeo Jupyter Book - that Ryan Abernathey has Created -->
- https://earth-env-data-science.github.io/intro


### Scott Henderson Medium Article

From

- https://medium.com/pangeo/intake-stac-nasa-4cd78d6246b7
- Scott Henderson - Dec 2020

### Overview
---

```yaml
--- 
Abstractions: 
  - openDataCube
  - stac-intake
Asset-Location: S3
Deployment-Technology: docker-compose
Format: COGS
Metadata-Containers: 
  - postgis-odc
  - stac-json
STAC_API_URL:
  - 'https://explorer.sandbox.dea.ga.gov.au/stac/'
  - 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
Sandboxes: 
  - cube-in-a-box
  - pangeo.chs.usgs.gov
  - etrocks-sandbox
Satellite: Sentinel-2A-2B
Topics: 
  - "Sentinel SCL"
  - ODC
  - Masking
  - Xarray-->netcdf
  - finding-clouds-in-the-cloud
```

---

# Featured Instructors - Key Points

- pandas, xarray, rasterio, matplotlib, holoviews - xarray.hvplot
- Innovative_Fast_solutions = open source + brainPower

- Olena and Steffi Model Verification
    - Significant as it directly and rapidly improves our scalable model code for Evapo
- Logan HLS 1.4 and 1.5 Research
- 

---

[https://www.usgs.gov/center-news/calibration-test-site-becomes-agricultural-hotspot?qt-news_science_products=2#qt-news_science_products](https://www.usgs.gov/center-news/calibration-test-site-becomes-agricultural-hotspot?qt-news_science_products=2#qt-news_science_products)



![](Assets/sentenel-scene-classification-levels.PNG)


---
### Open Data Cube (ODC) - glimpse

## Use Open Data Cube to extract Dwyer Cube from Sentinal S3 COGS

## Then use the big pangeo to explore Compositing with (Bunde, Postma, Danielson)

### ODC Outputs (netcdf/nc files in S3)
```
maine.nc
maine_ard.nc
maine_masked_s2_all_bands.nc
maine_s2_all_bands.nc
maine_s2_common_name_bands.nc
```

## maine_masked_s2_all_bands.nc
- main test nc file for compositing Maine - R&D only

- briefly understand cloud and shadow masking 

- [http://10.12.68.246:8080/notebooks/composite/30-cubebox-helper/2_tony_save_load_ard_all_bands.ipynb](http://10.12.68.246:8080/notebooks/composite/30-cubebox-helper/2_tony_save_load_ard_all_bands.ipynb)

- [http://10.12.68.246:8080/notebooks/composite/30-cubebox-helper/00_tony_class_exhibit_learning_odc_claibration_site_Sentinel_2.ipynb](http://10.12.68.246:8080/notebooks/composite/30-cubebox-helper/00_tony_class_exhibit_learning_odc_claibration_site_Sentinel_2.ipynb)






