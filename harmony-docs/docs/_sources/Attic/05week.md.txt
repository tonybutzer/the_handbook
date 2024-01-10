
## WEEK 5 - Data Wrangling is Underway - Understanding S3

## Happy Holidays
- looking forward to 2021
- thanks for particpating in these cloud activities - this effort is important


## Topics covered today - Major Theme - Data in S3
    
1. Silo Busting
1. IT Security in the Cloud - strategy/impacts
1. Pangeo and mini-pangeo when to use 
1. Logan demonstrates - viewing buckets via the AWS Console
1. Logan's notebook for examining a COG/nonCOG - xarray
1. Logan's methods for scaling/resampling vs. windowing/clipping
1. Tony - adventures in portal scraping for rapv2 and BITv3 - range-land herbs
1. Tony - presents notebook of the week - Pandas and Violin Graphs
    
     

## No silos; No Silos; NO SILOS!
- lets work together
- "many hands make light work"
- Good communication with CHS  - Eric Driscoll Larson's team
    - Thanks Neal
    - EROS cloud pilot projects are very important toward shaping science 
        - EROS is a WORLD CLASS DATA CENTER - we need to exert our influence
    - PANGEO, CHS Custom Pilots, CHS Science Data Lake, ESRI Integration
    - AI/ML
- Steffi Kagone - talk about the model we just ran over the weekend
    - The pontential for using Docker to scale in the cloud
    - Visualization effort - and outside synergies - Gabe, Darin
    - Sharing data between Science elements - Terry Sohl, Ward Sanford - Wes Zell - Greg Rouze
    - how it would be nice to have ESRI tools in the cloud with direct access for s3 bucket data/data lakes
    - In the Cloud Queue
        - VegDyn - Trenton, Dinesh
        - LandFire - Anyone in class from Landfire? - Neal invited as a consultant.
        - LCMAP
        - WaterSmart
    - Logan to train Steffi's team on VDI meets FileZilla and the cloud EC2 - ssh key managment etc.
        - Barter system for skill exchange - new staffing models needed to address the pace of change in technology

[CHS SERVICE LINK](https://taskmgr.chs.usgs.gov/servicedesk/customer/portal/10)


## Understanding COGs and NonCOGs
- data sizes and overviews

### A word about Data Compression

---

Below is a summary of the compression ratios of each method in the worst case: 
- 10-meter Sentinel-2 bands, 
- internal tiling and overviews.
---

| method | Compression Ration | Reason to use |
| ------| -----------| ---------------------|
| LZW 	| 1.16:1 | Quick to run and easy to adopt |
| DEFLATE | 1.38:1 | A slower but better performing alternative to LZW |
| ZSTD 	| 1.45:1 | Promising, CPU intensive but not mature |

    Table. Summary of the results of the different compression algorithms

---

## In the cloud you can test all compression techniques
- and change your mind - its fast and cheap to reprocess to other formats
- zarr is an interesting technology as well


### Email from my OpenDataCube Tasmanian Friend - Alex Leith
- Aussie lessons learned will likely influence LCMAP

Hey Tony

And hey Jeff [Briden] and Jon [Morton] of {LCMAP FAME}

Happy to talk about how we do ODC work in the cloud, including doing continental-scale data processing work.

We have some neat new examples using AWS tools like their Simple Queue Service along with Kubernetes to run a whole of Africa pixel quality analysis (so just visiting Sentinel-2's SCL band, over all pixels over Africa) and we're able to process that on 5 large EC2 instances in `~20 minutes, which is fun! Costs us $20 USD.`

Our land cover folks are doing something similar in Australia with LCCS, and I could bring them along. `They're science users, and are happy working with Python and the ODC` along with Kubernetes and job queues to run through that analysis, including iterating quite fast. I'm not sure about the costings of that, but it's been really successful this year!

So yes, happy to talk some time in the new year. Might need to be late Jan when we're all back on board!

Cheers,

---

## IT Security and Compliance Part II

### Logan and Tony - "WE GOT THIS!"

### IT Security is way easier in the cloud

- Paul Exter Email
    - SSM Agent and auto Updates
    - AmazonSSMManagedInstanceCore IAM Policy  attached to ec2 instances


[Shared+Responsibility+Model](https://support.chs.usgs.gov/display/CHSKB/Shared+Responsibility+Model)

- lower server footprint and vulnerability attack surface
- reduce user numbers in my Landsat mini-pangeos
- migrate users to big pangeo; teach cookbook examples in the Big Pangeo
- migrate eco users to the eco VPC mini-pangeo
- add encryption where i have to - or decomission less important services

### IAM - things you will never, ever, need to know - Whew!
- but if you do there's an app for that - I mean a Jupyter Notebook for that!
- aws iam list-attached-role-policies --role-name lsds-developer-ec2
- Jupyter notebooks simplify every complex concept :-)



## Kelcy - where do you author notebooks? 
- Answer: pangeo.cr.usgs.gov
- PANGEO  manged service - is nice because IT Security is someone elses problem
- Where is your S3 bucket?
- You are working on a STAC Collection 2 Example - Right?

### IT Security Goal
> Improve IT Security Compliance - with minor impacts to creativity, scaling and science

> Keep our eyes on the mission - not the distractions.

---

### The Oregon Pronunciation Conundrum - perhaps we should move to us-east-1
- because that is in Virginia
- I found out the 53% of the folks use the fake-pronunciation for Oregon
	- I am glad I am in the 12% who actually get it right. :-)
	- I am thinking about starting a Facebook campaign

![](Assets/AURA-gun.PNG)


- organ trail?
- or-AGAIN


**My friend once told me "You must be the most pedantic person in the entire world."**
- "Third most, actually." -- :-)

---

![](Assets/eco-custom-chs.jpg)

## Logan Data Wrangling, S3 and early validation notebooks

1. Logan demonstrates - viewing buckets via the AWS Console
1. Logan's notebook for examining a COG/nonCOG - xarray
1. Logan's methods for scaling/resampling vs. windowing/clipping

- S3 buckets view from the AWS Console
- Quick Sanity Check of NED Data
- in0 --> in1 (COGs) Model Ready Data Perhaps   `s3://eco-w1/in0/rapv2`; etc ....

## Wrangle rapv2 and mrlc_zip
- next week we will use the cloud to create COGs from these in parallel - via docker orchestration

- https://github.com/tonybutzer/logan/blob/main/00-notebooks/00-portal-scraping/00-MRLC-Notebooks/00-data-scraping-grab-zips.ipynb
- [LINK HERE](https://github.com/tonybutzer/logan/blob/main/00-notebooks/00-portal-scraping/00-MRLC-Notebooks/00-data-scraping-grab-zips.ipynb)

### A note about PANGEO FORGE data wrangling shared code
- Pangeo realizes that public data is slowly being organized in buckets and data wrangling still needs to be done.
- https://medium.com/pangeo/pangeo-2-0-2bedf099582d
    - [2016 Schedule of Pangeo genesis](https://rabernat.github.io/aospy-workshop/posts/workshop-program/)
    - cultivate ecosystem nextgen open-source tools, scalable, leverage geeks outside science
    - grassroots - scientists coming together - no silos
    - EarthCube - funded via NSF - long-term dialog between NSF and scientific communities
    - Originally HPC focused - but quickly gaining momentum in cloud computing and 
        - `"we quickly realized that cloud offered unprecedented ability to experiment with new modes of computing and data access."` - Ryan Abernathey
        - Zarr is on track to become an OGC Community Standard.
        - drive the adoption of and experimentation with new cloud-native array formats like Zarr, TileDB, and Cloud Optimized Geotiffi.
        - LCMAP investigating TileDB
        - We have also worked to improve tools related to loading and cataloging data, including fsspec, intake, intake-stac, intake-esm, etc.) 
        - Contribution to the development of interactive visualization tools as the Holoviz suite of tools, which allow interaction with massive data through the use of Datashader and Bokeh.
        - I would include panel and other dashboarding libraries/packages/modules HERE
        - Sophisticated CI systems - IaC.
        - Dozens of educational / training events around the world. (partial list, Pangeo YouTube playlist)
            - [Unorganized List Here](https://github.com/pangeo-data/pangeo/issues/440)

## Featured Notebook in Big Pangeo pangeo.chs.usgs.gov

- I have an account in pangeo.chs.usgs.gov
    - this is a nice capability for basic jupyter notebook training
- Steve Labahn got a Pangeo account at the click of a button
- This is a managed service and there are benefits - since many items are taken care of.
- I think you can request a bucket to go with your user ???
- You can definitely play with notebooks here

[ simple example plots big pangeo here](https://pangeo.chs.usgs.gov/user/butzer@contractor.usgs.gov/notebooks/opt/Oldstuff/notebook/00-Tutorial/01-Basic-Plotting-Python/00-example-plots-tony.ipynb)


## Superheros Notebook
- http://10.12.69.233/user/harmony/notebooks/opt/harmony-notebooks/00-pandas/00-demos/02-plotly-express/super_heros_pandas_plotly_espress_demo.ipynb
---

## END of WEEK 5
---

