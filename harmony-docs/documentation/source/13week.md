# Week 13 - day in the life of ETa

### subtitle - Don't Tell My Boss

## Real World Scene

- My boss - says I have to get Tmin, Tmax and Tavg - done for 150 years - converted to Celsius
    - from that useless Kelvin data i gave her - she is not happy
    - she says I have until COB Friday or look for another job
    - The problem is it looks like golfing weather for Monday and Tuesday
    - So I think use the cloud and docker - maybe this can be done 
    - I spend a day figuring out the sophisticated algebra and try to play that up - But she is on to me.
    - docker - container from jupyter to orchestration in 2 easy steps

### run the orchestration


> two system engineers walk into a bar

- ... the first one asks why can't we do that simple Kelvin conversion by friday on our current platform

- ... the second eng says cause x and y suck

- ... the next day the 2nd eng is explaining this converstion to his Govt Sponsor as:

    - well you see the Netapp is bandwidth constrained and not really intended for large image data xfers and Microsoft has chosen Linux as its highly scalable platform for its Azure Cloud.

## Community Interest
- Looking at Pangeo and Docker on HPC
    - Could support nice hybrid solutions between the cloud and HPC(s) Denali, Tallgrass
    - need to examine Singularity and Shifter on the HPC
    - I may call my orchestration method - manual_transmission :-)
- Tony prefers scaling with docker versus other methods - Why:
    - MPI – Message Passing Interface¶
        - Distributed Memory Systems
        - More difficult to parallelize
        - Requires a change in fundamental programming
    - Kubernetes is well over 1 MILLION lines of code
    - Slurm - the s stands for simple - is over 500,000 lines of code
    - Simple Orchestration -  129 lines of code

```
ubuntu@ip-10-12-69-188:/opt/kelvin_celsius/api$ wc -l kelvin_*.py
129 kelvin_orchestration.py
```


## Community Case Studies
- VegET in the cloud
    - Cloud Scaling
    - Model validation without ARC tools
    - Simple Visualizations
    - Pathfinder project for other cloud enthusiasts
- ETa pipeline from SSEBoP (Google Earth Engine)
    - Pushing data into a Dark Repo
        - Web Interface for endusers
        - Many data users just want direct access to COGs


## Day in the Life of the low budget ET project

---
![](./Assets/VegET-DRB-Rouze.PNG)
---

1. Port the VegET model from Windows and Netapp  - to cloud, xarray and S3 data storage
2. Run the model on small AOIs
3. Scale the Model by slicing the problem spatially 
    - glue the parts together with simple xarray code and multiple docker containers for scaling
4. Wrangle and Wrangle Data for Delaware, Conus, NorthAmerica, Globe
    - Also just to make it more challenging - add projected or future model data for temperature and precip
    - do this with as few people as possible with tight deadlines
5. Run the model for 150 years over Delaware
    - Notice some data model issues over 2000-2020
    - Visually apparent with jupyter-python-panel-app.ipynb
5. Run DRB again for 70 years times 2 with different soil intercept values.
6. Hire a `Model Integrity Analyst` Olena 
    - Write a simple pandas model simulator
        - replaces old windows manual excel spreadsheet methods
    - Discovered Kelvin and Celsius Confusion
    - ![](https://www.nasa.gov/sites/default/files/styles/side_image/public/thumbnails/image/1979_hst_primary_mirror.jpg?itok=UJ4wDauY)
7. Wrote a very simple Kelvin-->Celsius Conversion Python Notebook --> Python App with Argparse API
    - Run this in class today 1950 --> 2099
        - Notebook prototype/bread-board    
            - Slicing in python and xarray - time-series
            - simple docker image
            - basic orchestration 101
            - functional programming like `ds = ds - 273.15`
8. Convert to pure Python - Olena and add argparse to replace hardcoded values
    - jupyter nbconvert --to script  my_ugly_notebook.ipynb
9. Create an orchestration python wrapper - borrow an old one and customize this
