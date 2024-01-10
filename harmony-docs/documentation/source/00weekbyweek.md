<u>Week by Week</u>

# Class Syllabus

## Prerequisites - Suggested Reading/Viewing

### Pangeo, COGS and maybe Stac

![](https://github.com/tonybutzer/etscrum/raw/main/00-presentation/ard/abernathey-is-right.PNG)

---

![](https://raw.githubusercontent.com/tonybutzer/etscrum/main/00-presentation/ard/new-arch.PNG)

---
- The Future of Data-driven Discovery in the Cloud - Ryan Abernathey (Columbia University)
	- https://www.youtube.com/watch?v=7kDYfUe0Zhw
	- `The above youtube is worth watching - 14 minutes`


### COGs and ARD
- https://medium.com/planet-stories/cloud-native-geospatial-part-2-the-cloud-optimized-geotiff-6b3f15c696ed
- https://medium.com/planet-stories/towards-on-demand-analysis-ready-data-f94d6eb226fc

## Week by Week Class Summaries

### WEEK ONE
#### Week One Objectives

- FEEDBACK - send me direct chats with pithy comments that might improve our mission
- ESIP - don't hold back science - Rich Signell
- Discuss the goals for this class - success criteria - move one more science project to the cloud
- Comments and viewpoint of Neal Pastick
- Demos
	
	- [nginx on cloud server](http://10.12.69.188)
	- [jupyter notebook without the code](http://10.12.69.188/pie)
	- [ET Viewer Side by Side no timeseries sad](http://10.12.69.233/user/harmony/notebooks/notebook/00-Viz/96-hvplot-experiment-image-annual-et-viewer-decorator-version.ipynb)
	- [time series panel demo - little code](http://10.12.69.233/user/harmony/notebooks/notebook/00-Viz/panel-timeseries-get-x-y-and-plot.ipynb)

	- I will move some of these to Neal's interim web servers
- Discuss the Student cross section
	- http://184.83.30.149:57778/00define_ET.html#students
	- http://184.83.30.149:57778/00define_ET.html#student-individual-goals
<img src="https://raw.githubusercontent.com/tonybutzer/etscrum/main/00-presentation/bonus-slides/case-study-1.PNG">

- Discuss two Case Studies - Commonalities and Not
	- Evapo
	- permaFrost
- Contact Tony Butzer for cloud questions
- Discuss notebook love hate meter - any notebook shy/sensitive folks?
	- its just a tool; "you're a tool tony"
	- `There will be lots and lots of notebooks in this class`
- Point to the two computers - field any questions
	- web http://184.83.30.149:57778 hweb
		- [AWS on-boarding website paper --LINK](http://184.83.30.149:57778)
	- mini-pangeo 10.12.69.233 harmony
		- [mini-pangeo --LINK](http://10.12.69.233)
- Computer Access Methods
	- Jupyter via browser and url and `VPN`
	- Terminal inside Jupyter
	- direct ssh and scp access - public key
		- ssh ubuntu@10.12.69.216
		- ssh ubuntu@10.12.69.233
	- open ports allowed via firewalls
		- 80, 8080 http
		- 443, 8443 https
		- 22 ssh,scp
	- use of `tmux` for session preservation across network/VPN failures/timeouts - long running jobs

- Point to the website - nginx/sphinx driven
	- [AWS on-boarding The website paper --LINK](http://http://184.83.30.149:57778)
- Point to the github - 
	- [https://github.com/tonybutzer/harmony](https://github.com/tonybutzer/harmony)
- Quick Jupyter Session - jupyter fitting from single jupyter -- to self scaling hubs
	- focus here will be primarily mini-pangeo scope - a group of 13 students
- Self-directed study hints
	- notebook repo - past pangeo training
		- If you need one on one jupyter training I can arrange an hour with you
	- github link - needs pruning - notebook repo here: 
		- [https://github.com/tonybutzer/notebook/tree/master/00-Tutorial/00-Jupyter-Notebook-Pieschke](https://github.com/tonybutzer/notebook/tree/master/00-Tutorial/00-Jupyter-Notebook-Pieschke)
		- [https://github.com/tonybutzer/notebook](https://github.com/tonybutzer/notebook)
		- Tony can help you find just the right example or create it for you.
		- We wil use some of these examples in class and the Labs
- future todo - feedback based
	- create very small notebook snippets that illustrate concepts
	- refine sections of this "paper" and build examples
1. Project Kickoff and refinement of goals
	- Is this anything? - trial and error Seinfeld
		- doing this class is scary must be what its like to do stand-up comedy
		- this class is `new` sort of a science experiment in itself
	- `PRIOR Experience`
		- linux
		- docker
		- AWS
		- python
		- jupyter
		- management/leadership
	- `I want to build a notebook that radar charts the students`
	- Class questionnaire - via email - or maybe a notebook
	- Communication preference of each student
	- efficiency and boredom mitigation
		- perhaps split each 1 hour into - concepts and practice - allow folks to bail at 1/2 way point
		- perhaps - threads or channels
			- jupyter thread
			- linux thread
			- docker thread
			- devops thread
			- python thread
			- management leadership - steering committee thread for PANGEO - strategy

	- I want Neal to drive most of the agenda and deep dive talks - at least initially - people can opt out
		- for example I could write a chapter on costs in AWS
			-perhaps most would be interested - I know Neal is
1. Week ONE - DEC 1,2020 Introduction and Basic Cloud Tour 
	- Quick overview of this document
		- added a glossary
		- please skim
		- if you have comments or questions - please use Teams/Chat to contact me
			- I will likely post some of the converstaions in this document
	- Neal's team won a free mini-pangeo
		- terraform 
		- the littleist jupyter hub - intro
	- Neal wanted a kanban too/also
	- SEE DEVOPS WEEKLY
		- [DEVOPS LINK](http://184.83.30.149:57778/27etops.html?highlight=devops)

## Teams Note
Hey Class: - the course website is starting to take shape and is here:
- http://184.83.30.149:57778
	
we will fill in more color/detail as we go through our CASE Studies.
- our companion github repo is here - can't live in the cloud without github/dockerhub.
	- https://github.com/tonybutzer/harmony

---
- this is also where our cache of notebooks will live - like this one:
	- https://github.com/tonybutzer/harmony/blob/main/class/06-Instructor/01-Students.ipynb
	- https://nbviewer.jupyter.org/github/tonybutzer/harmony/blob/main/class/06-Instructor/01-Students.ipynb
---
	- See you all on tuesday December 1st at 12 NOON 
	- See you next week for an open lab
	- The week after that I will look at Areas of Interest and how they relate to ET modeling
---
## WEEK TWO 

## Preface

### The cross organization and cross project communication is way more important than the technology lessons
- working together and sharing talent
- moving to the cloud where its natural to share everything
- creating libraries and documentation for the common good of the data center
- allowing our hard work in science to be broadcasted to the widest possible audience
- removing data and people silos wherever and whenever we can

### Welcome to the JupyterHub and Pangeo 
- extraordinary week 2
- let the fun begin

## Outline

### For Neal's Project ( Case study one projects journey into the clouds )
1. Acquire a CHS CUSTOM ACCOUNT and a Project VPC `[DONE]`
2. Setup 2 computers - a tiny admin box and jupyterHub micro-pangeo
3. Project Management steps rapidly developed via a sphinx website - backed up in git
4. Spin up a jupyter hub for coding and engineering collaboration
5. layout the data pipline big steps and refine a simple WBS/todo-list to execute.
6. Spin up a quick Kanboard to track actions and report progress to Neal

<!--
#### Details Example
> [Yesterday 4:11 PM] Pastick, Neal (Contractor) J
    Those data wrangling, pre-processing steps (e.g. re-projection if needed, spatial extent alignment), and database development are all that needed before performing modelling in this simple example. That is, once I have the tabular database developed through extraction of geospatial at each field plot, I can commence model calibration/validation/deployment. 
​[Yesterday 4:18 PM] Pastick, Neal (Contractor) J
    Guess I was a little vague w/ the raster pre-processing steps - can't recall what the resolution or projection is of all those datasets. The biggest thing might be to clip the data to a common extent - using a shapefile that we upload - and reprojecting and resampling things. No hard core per-pixel compositing methods needed here.
​[Yesterday 4:20 PM] Pastick, Neal (Contractor) J
    Could also stack all those data into a giant xarray for model inference later on - might be overkill as I should be able to point the models to the individual datasets
-->

- `Deep Thoughts` by Neal Pastick
	- Key takeaways from last week
	- Motivating words to inspire the troops to forge ahead.
	- CHS CUSTOM Account status
		- next steps
		- [terraform](http://184.83.30.149:57778/13glossary.html?highlight=terraform)
	- Phases for the Data and Processing from:
		- portal scraping, ftp transfers to buckets `this is mostly a solved problem`
			- this is also easier in the cloud - can be done in parallel -- multithreaded
		- ...
		- SageMaker ML and voila moments
- Michelle Anthony - any thoughts or questions about how this **disruptive** technology might vector your mid-term roadmap?
- Matt Rigge - can you talk about your role and your team and your pipeline you are targeting for cloud operation.
- Dev Dahal - talk about logging into Jupyter - opening a terminal and cloning a repo and what you hope to use this class for in your real job
- Tree Regrowth - When I get my SDSU students (perhaps...)
- [seaborn plot gallery](https://seaborn.pydata.org/examples/index.html)
- Anyone else?
	- We talked about a bunch of stuff in week 1
	- Anything we need to clarify about the cloud, AWS or CHS?
	- feedback ... or ... takeaways?
- Example panel based applications
	- Glaciers
		- [https://edu.oggm.org/en/latest/explorer.html](https://edu.oggm.org/en/latest/explorer.html)
		- similar to some of our WMS apps with far less backend engineering - scaffolding
	- Data Viz applets
		- widgets
		- graph display libraries
		- SDSU viz expert team - coming soon
- Gradually these classes should become more democratic - with lots of individuals taking the mic.
- Review last Week
	- pangeo is great
	- cloud is great
	- public data assets stored in the cloud == game changing paradigm
		- you MUST start to use cloud, readily available (fingertips), analysis ready remote sensing data assets - or be left behind
		- L8
		- Collection02
			- [landsat-commercial-cloud-data-access](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-commercial-cloud-data-access)
		- Sentinel
		- HLS ...bump ...bump ... YES
		- Evporation Model Outputs - after they go thru ScienceBase validation - but maybe even raw for evaluation
	- one computer to rule them all - t3a.2xlarge
		- [https://aws.amazon.com/ec2/instance-types/t3/](https://aws.amazon.com/ec2/instance-types/)
		- 8 CPU, 32Gig Memory, 200Gig local-ebs-elastic-block-storage  - with S3 access
	- technology zen equation
```python
science_joy = 1 * ec2 + docker * 1e3
```

### A World of Twos
- two computers
	- t2.micro
	- t3a-2xlarge
- two infrastructure elements
	- ec2
	- docker
- two technology companions
	- jupyter
	- python
- two science - image processing packages; fundamental building blocks.
	- xarray
	- pandas
- two people - who are "ALL IN" on the Cloud!
	- tony butzer
	- Rich Signell
- two barriers toward cloud acceptance
	- jargon
	- complexity

### Special Recognition for Kelcy (AWS CHS Credentials)
- implications for data movent to and from buckets directly from servers on-prem at EROS

### "Hey Tony; can I have an account on AWS onboard mini-pangeo?"
- "Yep, Yes, Si, qui, Ja"
- ## हो   
- ## Hō

---


## Student Getting Started Instructions
#### Signing into the jupyterhub-mini-pangeo

- 10.12.69.233
    - username is '[LASTNAME]'
    - password is `harmony`


### git repo clone

- clone our notebook repo
- next week we will do a `git pull` for updates

### Instructions

![](./Assets/new-term.PNG)

#### open a terminal in jupyter
    - find Home Page - browser tab - or middle click jupyterhub above - tony to demo
    - [new] button - terminal
    - pwd ; ls; 
---
- mkdir opt
- cd opt
- git clone http://github.com/tonybutzer/notebook
---

### Don't feel like cloning sheep
---

<img src="https://dolly.roslin.ed.ac.uk/wp-content/uploads/2016/01/Dolly-and-surrogate-mother-768x915.jpg" width=10% style="vertical-align:middle">

<img src="https://dolly.roslin.ed.ac.uk/wp-content/uploads/2016/01/Dolly-and-surrogate-mother-768x915.jpg" width=10% style="vertical-align:middle">


## Just use group login:

- http://10.12.69.233
- harmony
- harmony
---

## Winner Winner Chicken Dinner
- that is all I wanted to get accomplished
- Everything else this week is a bonus!


---
## One on one sessions and jupyter tours available

- just open a chat with tony butzer for custom notebook tour relevant to your technology interests

## If I can Help you to the cloud - just ask
- its free free free - I am funded by OpenDataCube
---
## Rules of Behaviour and IT Security Training

- its a priviledge to work in a sponsored cloud
- Be Responsible not malicious
- Save the Planet with Science - Please!

- oh and if computer or language things break - use the TEAMS-CHAT - to tonybutzer
---

## How to cheat at Markdown
- Markdown is another zen item in the technology universe.
- below are two simple tables in markdown
- and a great editor for learning markdown in 10 minutes
	- [https://jonschlinkert.github.io/remarkable/demo/](https://jonschlinkert.github.io/remarkable/demo/)
- and as always all you need is a browser
	- We don't need no education
	- We don't need no thought control
	- No dark sarcasm in the classroom
	- Teachers leave them kids alone… -- Pink Floyd --

```
| sign | poet-line |
| ------:| -----------:|
| > | When the Star Belly Sneetches had frankfurter roasts
| > | Or picnics or parties or marshmallow toasts,
| > | They never invited the Plain-Belly Sneetches
| > | They left them out cold, in the dark of the beaches.
| > | They kept them away. 
| > | Never let them come near.
| > | And that’s how they treated them year after year.
| > | -- Dr. Seuss --
```

```
| sign | poet-line |
| ------| -----------|
| > | When the Star Belly Sneetches had frankfurter roasts
| > | Or picnics or parties or marshmallow toasts,
| > | They never invited the Plain-Belly Sneetches
| > | They left them out cold, in the dark of the beaches.
| > | They kept them away.
| > | Never let them come near.
| > | And that’s how they treated them year after year.
| > | -- Dr. Seuss --
```


### https://jonschlinkert.github.io/remarkable/demo/  -- [Clear] - 
- [https://jonschlinkert.github.io/remarkable/demo/](https://jonschlinkert.github.io/remarkable/demo/)
- try the above text in the remarkable wysiwig tool

---


## Science should be done with pandas and xarray

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/600px-Pandas_logo.svg.png)

![](http://xarray.pydata.org/en/stable/_static/dataset-diagram-logo.png)

### XARRAY 
- I'm doing science with `xarray`
	- xarray is like the Chicago airport - its not your final destination - but you can get anywhere from there
- everything else in python is just **glue**

## Notebook Drive By 

## Notebooks are:
- like storyboards for the real movie
- teaching vehicle to illustrate code and its outputs
- tool for rapid application development and collaboration
- the on-ramp to exciting panel applications
- a way to quickly teleport to your cloud computer with just a browser - even from the beach

### My best notebook to date
- and i have written hundreds of notebooks

#### [zen](http://10.12.69.233/user/harmony/notebooks/notebook/00-Harmony/02-week2/03-zen.ipynb)

### Xarray Basic - hello xarray
#### [gentle intro to xarray](http://10.12.69.233/user/harmony/notebooks/notebook/00-Harmony/02-week2/01-gentle-intro-to-XARRAY.ipynb)


### A word on public data assets
- public - that sounds nice
- planet really pushed this pangeo world - thanks planet
- [https://registry.opendata.aws/landsat-8/](https://registry.opendata.aws/landsat-8/)
### Notebook illustrates Pangeo, Xarray, Public Data Assets and Panda
- this notebook was featured by tony butzer at AR19
- the point is that when we move the Scientist to the data
	- everyone wins because so much more science and collaboration can be done
- Can xarray, pangeo and python help automate change detection pipelines for tree regrowth for Dr. Zhou?
- 

#### [pine-lake](http://10.12.69.233/user/harmony/notebooks/notebook/01-Everything-but-harmony/10-DEMO-lite-stac-xarray-all-sandbox/000-demo-pine-lake.ipynb)




## Jupyter Roles/Features/Capabilities
- text editor
- python coding and exploring
- teaching/collaborating tool - commands and output in the same place - writes text books as you go
- file transfer agent - upload and download files 
- web app development accelerator - panel package
- teleports people with a simple browser right inside their free computer
- AWS onboarding enabler - view the cloud - see the grand canyon without getting hurt
- terminal and bash access
- poor man's powerpoint tool
- and for `Science` - well that is what **jup** was **born for** - for those that realize it anyway
- ... and so much more ...  "A lot of people say this Jupyter thing is going to be huge -- its fantastic! -- who knew?" 


---
## END OF WEEK2

### Thank You Everyone

- i will sort out week 3 now!
---


## WEEK 3 - Meet Logan


## Logan's assignment:
### Data Wrangling --> Portal Scraping

- Logan needs to download Neal's invasive AOI input data
	- This week he will load rangeland cover v2.0 
		- Band 1 --> annual forb and grass
			- forb - herbaceous flowering plants
- Fortunately Neal only needs Band 1 from the image and a small subset windowed
	- else its half of CONUS and 136 Gigabytes per file
- Also fortunately the web site has a Readme file with an example `gdal_translate` command

---

## Crowd Source

- http://10.12.69.233/user/harmony/tree/opt/logan/00-notebooks/00-portal-scraping/00-MRLC-Notebooks/IMG

### Logan Writes
> [10:13 AM] Megard, Logan J
> Looks like to convert the .img you can either use  [gdal_translate -of GTiff Test.img New.tif] or [rio convert Test.img rio.tif]

- Matt Rigge is correct unzipping is an extra burden
- Also did I mention proprietary data formats are an extra pain
	- we don't like vendor lockin strategies in an Open Systems World

---

## Review Prior Week(s)
### You should work in the cloud
- A CHS CUSTOM account is useful
- Jupyter and Python are nice
	- Tony's role is to guide you up the learning curve
		- and then turn you loose to use science to save the planet
## Summary 
- This week we demonstrate how easy it is to work in the cloud
	-  by using geojson to quickly display extents:
		- Our huge source files that are 1/2 of CONUS
		- Our semi-big general Area of Interest (AOI)
		- Our smaller school/class size imagery to be stuffed in an Xarray - what else?

### We also explore command line tools for
- gotta learn to love the cli if you want to be a power user - of just about any tool
- GDAL window slurping accross the net
- rio for getting the extent bounds into a geojson
- aws s3 ls (plus cp, mv, rm, cat) for seeing things in our s3 buckets
	- Logan notices the `s3 commands` are a direct corollary/map to the `LINUX commands` for files
- vsicurl and vsis3 and s3:// 

### We will also build on things we learned in week one and week two 
<img src='https://carboncostume.com/wordpress/wp-content/uploads/2013/09/Thing-One-and-Thing-Two.jpg' width=20%>

### Finally; we will explore a bucket of portal scraped inputs

```
aws s3 ls s3://dev-et-data/logan/in/raw/
```


## Since this class is about case studies
- This week lets switch to following our Invasive Machine-Learning (SageMaker) AWS Project
- Neal is working with CHS to get his cloud space started up with a very small server
- Then Logan will create and destroy on-demand computers at will for Neal and the Team

## Quick a word about rio

- `rio is the command line tool - swiss army knife for data wranglers`
- like gdal for dummies; build on rasterio/gdal

- ! rio --help

```
Usage: rio [OPTIONS] COMMAND [ARGS]...

  Rasterio command line interface.

Options:
  -v, --verbose           Increase verbosity.
  -q, --quiet             Decrease verbosity.
  --aws-profile TEXT      Select a profile from the AWS credentials file
  --aws-no-sign-requests  Make requests anonymously
  --aws-requester-pays    Requester pays data transfer costs
  --version               Show the version and exit.
  --gdal-version
  --help                  Show this message and exit.

Commands:
  blocks     Write dataset blocks as GeoJSON features.
  bounds     Write bounding boxes to stdout as GeoJSON.
  calc       Raster data calculator.
  clip       Clip a raster to given bounds.
  convert    Copy and convert raster dataset.
  edit-info  Edit dataset metadata.
  env        Print information about the Rasterio environment.
  gcps       Print ground control points as GeoJSON.
  info       Print information about a data file.
  insp       Open a data file and start an interpreter.
  mask       Mask in raster using features.
  merge      Merge a stack of raster datasets.
  overview   Construct overviews in an existing dataset.
  rasterize  Rasterize features.
  rm         Delete a dataset.
  sample     Sample a dataset.
  shapes     Write shapes extracted from bands or masks.
  stack      Stack a number of bands into a multiband dataset.
  transform  Transform coordinates.
  warp       Warp a raster dataset.
```


## Objectives - 
1. Answer some of the staffing needs in the cloud.
	- The pace of technology means skill workers need to constantly tune-up their skills.
	- This means a steady diet of self training via
		- Google
		- Youtube
		- and classes like this one :-)
2. Look At Data Wrangling 
	- Current State 
	- Future State
3. Cool Notebook of the week and WHY its cool!


## Logan is a Senior GIS DevOps Dude 
- Logan works on science projects in the cloud
- currently invasives and then permafrost
- Logan is a full-stack engineer - still honing his skills but he has a high aptitude and a thirst for knowledge
- Lets follow Logan with his new AWS account as he sets his project up for success

## A day in the life of Logan the data slayer

### Logan sets up his git repo
- [https://github.com/tonybutzer/logan](https://github.com/tonybutzer/logan)
- [https://github.com/tonybutzer/logan/tree/main/00-notebooks/00-portal-scraping](https://github.com/tonybutzer/logan/tree/main/00-notebooks/00-portal-scraping)

- logan reviews Neal-Bruce-Dev-Rigge-et-al-half-of-eros-paper-here
	- [exotic phenology](https://github.com/tonybutzer/logan/blob/main/00-notebooks/00-portal-scraping/Characterizing_Land_Surface_Phenology_and_Exotic_A.pdf)

## Logan's coolest notebooks
[readme notebook](https://github.com/tonybutzer/logan/blob/main/00-notebooks/00-portal-scraping/00-readme.ipynb)


### Logan creates his new server

#### Selects t3a.xlarge with 400 Gig of disk

- [https://calculator.aws/#/](https://calculator.aws/#/)
- his t3a `[t3a.xlarge]` machine will cost $141.79 - Logan doubles that for his boss and says $300/month
- Logan remembers that the desktop tax they used to charge projects was $4000/year - 
- Logan also notes this will be for 4-5 science users
- Logan wonders if he should bring up reserved instances and decides - "well I'll have that in my pocket"

#### Logan ponders on the nuanced complexities of the AWS ec2 service landscape
- Logan keeps repeating - keep it simple - keep it small - tony's influence perhaps
- Logan thinks - "ok so for a standard-reserved and everything up to on-demand it would be $100 to $111 to $141"
	- Logan decides it will cost more to meet on all these service model variances than the dollars it saves.
	- Logan thinks about this decision and again Logan decides ...
		- it will cost more to meet on this than the dollars it saves.

Now that logan has determined his main ec2 computer and calculated the costs its time to spin up the system and bring up some foundation technologies.

#### Terraform Init & Apply

- Demo Here?
- Picture of Logan bringing up ec2 instances for Invasives
![harry](./Assets/harry-potter.gif)


## Logan now wants to train his users 
- and the scientists on his team are a tough crowd
- logan does not like propietary formats
	- ERDAS IMAGINE
	- ESRI Shapefile
- logan likes geojson and geotiff files - FOR EVERYTHING
- logan can create and download geojson files using this site
	- [http://geojson.io](http://geojson.io)

## Logan borrows some material from USGS Workshops
### Scientific Software Environment of the Future - Rich Signell

### USGS:

- Try: https://pangeo.chs.usgs.gov

- Examples: https://code.chs.usgs.gov/pangeo/notebooks

- Join: USGS Pangeo Team: GS-Pangeo

## Larger Community:

- Follow: medium.com/pangeo

- Discuss: discourse.pangeo.io

- Chat: gitter.im/pangeo-data


## Logan starts to look at Data Wrangling 
- ### 1st stop portal scraping

- Logan sighs and wishes everything was just in COGs and used STAC - but you can't change the science world overnight
- Logan shoots Dev Dahal a quick email with links to his favorite public data sets:
- GA will compare our Collection02 STAC work against these public data assets:
	- [https://registry.opendata.aws/sentinel-2/](https://registry.opendata.aws/sentinel-2/)
	- [https://registry.opendata.aws/landsat-8/](https://registry.opendata.aws/landsat-8/)
- Then its back to work.

### Logan 00-notebooks/00-portal-scraping

#### github

- Logan notices some of these files are absolutely HUGE 
	- wonders about costs of storing
	- studies this S3 document - [AmazonS3](https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html)

	- Logan needs to use these linux commands
```
ls -lh
du -hd 2 .
df -h .
free -h
lscpu
uptime
top
```
Logan trys these commands by bringing up a terminal
- He thinks his students should play with those commands in the terminal
	- He also thinks he himself should get familiar with those in case people ask him to explain this Linux stuff
- How to display AOI in Jupyter
	- geojson and shapefile
	- folium
	- docker 

---
## Why Libraries/packages
- code reuse is easier
- keep notebooks smaller and they flow better for the reader
- abstact complex code
- installable with `pip`
- example library
	- [https://github.com/tonybutzer/logan/blob/main/loganLib/loganLib/fm_map.py](https://github.com/tonybutzer/logan/blob/main/loganLib/loganLib/fm_map.py)

---
## Featured Notebooks
### nbviewer.jupyter.org
- [geojson extent1](https://nbviewer.jupyter.org/github/tonybutzer/logan/blob/main/00-notebooks/00-portal-scraping/00-geojson-using-lib-logans-extents-displayed.ipynb)

---


### Runable as user harmony

- [geojson extetnt1](http://10.12.69.233/user/harmony/notebooks/opt/logan/00-notebooks/00-portal-scraping/00-geojson-using-lib-logans-extents-displayed.ipynb)
- [annual herbacious](http://10.12.69.233/user/harmony/notebooks/opt/logan/00-notebooks/00-portal-scraping/01-download-trials-annual-herbacious.ipynb)

- [xarray 12 band](http://10.12.69.233/user/harmony/notebooks/opt/logan/00-notebooks/00-portal-scraping/01-xarray-101.ipynb#Later-we-choose-some-cmaps---palletes---here-are-some-of-the-options)
- [folium markers](http://10.12.69.233/user/harmony/notebooks/opt/logan/00-notebooks/00-portal-scraping/00-geojson-using-lib-logans-extents-displayed-Marker-example.ipynb)



## Logan uses Jupyter to "bread-board" his python
- then he creates python libraries/packages with setuptools and setup.py
- Logan wants to show his fellow scientist how this is done 
- and don't foget building and orchestrating docker containers - Logan makes a mental note

- [Makefile](https://github.com/tonybutzer/logan/blob/main/api/Makefile)
- [wr_rangeland.py](https://github.com/tonybutzer/logan/blob/main/api/wr_rangeland.py)



---

## END OF WEEK 3

- next week we will look at more xarray code - and Logan's additional wrangling steps
---

## WEEK 4 - Standing up Your First Instance in the Cloud

## You really should be doing science in `the cloud`

## LCMAP to move to the cloud and use S3 and Xarray - Jon Morton

## Related Efforts 

- Project Thundercloud

![](Assets/thunder_cloud.PNG)

https://marine.usgs.gov/coastalchangehazardsportal/

>  *"Science, not operations.  Changing, not fixed.   And the world, not local.   We want to get to a flexible computing platform that lets us pay only for what we use, but lets us use whatever we want.  Lets us experiment, lets us scale, lets us not wait in queues, and lets us do our research as efficiently and effectively as we can.  And a platform where we can join other agencies and partners from around the world to share data, tools and approaches to help understand and protect our planet.  This is what the Cloud has to offer."* -- **Rob Thieler, Center Director, USGS WHCMSC, remarks delivered at the NHMA Fall 2020 meeting**


![rob](https://prd-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/styles/side_image/public/thumbnails/image/Rob-Thieler.jpg)

## Data Wrangling Tip of The Week 
- Jennifer Rover and Kelcy Smith
	- Pixel location --> it varies - especially in proprietary data format headers
	- know what your pipeline creates - lest you be a propagator of garbage
	- nudge a pixel if its off center and not alligned with the rest of your data friends


## Network tip of the week
- pushing data to the cloud is faster from EROS OA then thru the VPN - duh!
	- the 152.61.40.0 network is called the Office Automation Network 
		- it has access to the cloud CHS
	- the 137.227.0.0/16 address space is via the VPN and its considerably slower  
- Logan pointed out that the speed of then net was faster from his VDI
	- so we used putty, puttygen, pageant, filezilla and port 22 to xfer files up
	- after we created another t3a-2xlarge with terraform out of thin air.

### So use the VDI and FileZilla for pre-wrangled data on a windows network share Y: W: ...

## Using the AWS Console to Create 

### Introducing Logan Megard by Neal Pastick
- What's going on in your project Neal
- Only One week with AWS and we already have our instances up
- GIS Expert 
- Emerging DevOps Cloud Engineer

### Picture of the AWS Console
![aws](Assets/aws_console.PNG)


```bash
1. Create ssh-keygen to make an ssh key for your command prompt
	Save the ssh key so the key can be added to your instance
		so you can log onto it once its added

2. Log onto aws console. Select region (Oregon West), 
	Go to dashboard and EC2.
	create key pairs (Save keypair)

3. Launch instance, free tier only
	ubuntu 18
	t2 micro
	Need a vpc and subnet
	storage
	tags
	Security
	review and launch
	add key pair (one I already have)

4. connect via .pem location
	need to be in file location
	launch initial instance

5. set up new keygen
	cat authorized_keys or cat ~/.ssh/authorized_keys
	vi authorized_key

6. cd /opt
	git clone https://github.com/tonybutzer/logan
	ls
	dir
	
7. sudo apt update
	sudo apt install python3

8. ping 8.8.8.8
	history
	lscpu
	uptime
	
9. logout
	stop instance
	terminate instance

Done :)
		


```

---

## Logan captures great notes to be used as a cheat sheet
### Logan heard that Steffi Kagone has some notes as well

---
```bash
Names:
ssh -i megard-uswest-keypair.pem ubuntu@10.12.68.132
	log into inital instance for Ec2
	need the .pem key to log on the first time

cat authorized_keys or cat ~/.ssh/authorized_keys
	shows .pem and other ssh keys added

ssh-keygen
	creates ssh key for your cmd (keep a copy to add to the server)

ssh-rsa
	shows key

vi authorized_key
	adds 

ssh ubuntu@[ip_address]
	log into ip address (Ec2 instance)

uptime
	shows time for ec2 instance

lscpu
	shows build of ec2 instance (cpu, memory ...)

who
	shows who is on the server

w
	shows how much cpu and memory is being used and by what

ping 8.8.8.8
	shows speed test of server (ctr+d or ctr+c to exit)



logout
	leave server (Ec2 instance)

sudo apt update
	looks for update for packages

sudo apt install [python3]
	installs package

pwd
	print working directory

cd
	moves into the folder

git clone [http address]
	Copies git folder to current directory

ls
	shows whats in current directory

dir 
	shows everything in directory

more [file]
	displays a text file stopping at a page of the screen

cat [file]
	stands for concatinate and print to screen - same as more but does not use a PAGER


history
	prints out full history of commands in session



Custom:

pinstance
	- status - shows all ec2 instances in the VPC #eco in this case.
	- start - starts an instance - spins it up
	- stop - stops an instance - spins it down - #AWS does not charge money for spun down instances

pin - bash alias for pinstance status | grep -A1 megard
```

## PANGEO MISSION STATEMENT

> *Our mission is to cultivate an ecosystem in which the next generation of open-source analysis tools for ocean, atmosphere and climate science can be developed, distributed, and sustained. These tools must be scalable in order to meet the current and future challenges of big data, and these solutions should leverage the existing expertise outside of the geoscience community.*

---

## Stuart Udahl

> *Plans to protect air and water, wilderness and wildlife are in fact plans to protect man.*

---
## END of WEEK 4 - Happy Holidays
---

---
### Interstitial

<img src="https://miro.medium.com/max/1200/1*M9Clwvz95IGShrVqQ-4VIw.png" width=50%>

Examples of common forbs: 
- poison oak (top left), -
- western ragweed (top right), 
- silverleaf croton (bottom left) 
- and green briar (bottom right)


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

