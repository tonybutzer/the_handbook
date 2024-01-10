# Aws PANGEO Binder Demo

### This demo is about the scientist consuming data!

Historically the Scientist spent TOO MUCH TIME:

1. Curating Data - 80%

![curation](https://tr3.cbsistatic.com/hub/i/r/2016/05/25/805d84c4-4433-4e88-8deb-beba35642fd7/resize/770x/8310bac8293c2ff33234a742de31e1a6/dataproc.jpg)

2. Infrastructure - 10%
![infra](https://www.veritis.com/wp-content/uploads/2019/06/it-infrastructure-services-1.png)

## What if the Scientist could just do science?
![science](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTE9IfrG_7Uia2s6Ci5q6GF866QJRmCrrRbRcXpDL1I7OuONQjJ)


## Notebooks

1. Derivative Products
	- LCMAP
	- WOFS
	- Classifications - Fractional Coverages
	- Mosaics and Composites
	- NDVI thingies
2. Tutorials
3. Prototypes and Demos
4. Code fragments - future libraries
5. and many more ...

## Sandboxes

### In search of the perfect sandbox

1. easy to use
2. powerful
3. free
4. someone else's problem - sandbox technology stack is hard


### Candidates

#### None are perfect yet - but this one is closer

1. frontiersi
2. pangeo.chs.usgs.gov # DEFUNCT
3. ESIPs Pangeo
	- us-west-2
	- THIS ONE - aws binder us-west-2
	- Google Pangeo
	- HPC Pangeo
4. private notebooks - see contingencies

### Hey Tony, How we gonna do that Lunch-&-Learn?


## PANGEO LINK

[PANGEO](https://github.com/tonybutzer/notebook/blob/master/aboutPangeo.md)

```
if ( PANGEO == cool_sandboxes):
	print("Please Play in one of these with jupyter")
	print("ipynb is an extension from the old ipython kernel")
```


## Mission

### Save the Planet
### Enable Science

### Make Data Available - no curation 
### Make Data Useful - Analysis Ready Data - with STAC

### Make Infrastructure Simple
1. push button
2. always available
3. customizable
4. network effect - common meeting places - watering holes for scientists
5. us-west-2 (AWS)
6. Google Earth Engine - not sanctioned by USGS

## Why Pangeo is  Cool

1. democatizes science - all you need is a chromebook from the gates foundation
2. instant infrastructure - elastic - scales up - scales down
3. personalized, customizable
4. zero footprint
5. its in us-west-2 - all the cool scientists will be hanging there


## Requisites

standing on the shoulders ...

1. github
2. dockerhub
3. pangeo
    - aws
    - binder
    - pangeo.io
4. jupyter (notebooks, labs, hubs)


## Contingencies

- Riz1 Cloud Instance
- llsrlscd04 - local virtual machine with docker

### If there is time
```
thirty_mins = 60 * 30
if (time < thirty_mins):
	demo_llsrlscd04(dockerhub='tbutzer/jupyter-lite')
```

![null](https://www.hanselman.com/blog/content/binary/Windows-Live-Writer/f7e432634b00_9C16/image_4.png)

"It turns out," he continues, "the less that you do, the more of it that you can do. This is the standard law of scale."

What if you just had?

1. Dockerfile
2. Makefile
3. Markdown


## Specific Ingredients

### Howto

http://aws-uswest2-binder.pangeo.io

### My binder test repos


https://github.com/tonybutzer/notebook.git

https://github.com/tonybutzer/lunch.git


# Demo Script

## Start labs for above repos

## Binder (directories)

https://github.com/tonybutzer/notebook/tree/master/binder

https://github.com/tonybutzer/lunch/tree/master/binder

## Plotting


1. venn diagram
2. pie chart
3. radar chart
4. pokeman data scientist

## Xarray = Hanoi

## Further ODC study

1. Pangeo itself
2. Creating CONTAINED, REPEATABLE, JupyterHubs in CHS
3. STAC ecosystems and evolution
4. AWS technology selection criteria - cloud strategies for portability


## Tricks

```
curl ifconfig.co
```

https://zapier.com/blog/scale-yourself-scott-hanselman/

## How's GA Doing - what ever happened to that Africa stuff?

```

Leith Alex <Alex.Leith@ga.gov.au>
Wed, Oct 16, 5:30 PM (10 hours ago)
to me, Gavin

Hey Tony

The story I'm telling in a little presentation this evening is this:

-- Running the process on 3 on-demand EC2s took 50 hours and cost $200 USD
-- Running the process on 10 spot EC2s took 5 hours and cost $20 USD.

So that's ~2 orders of magnitude better, if cost and time are equal!

We ran 400-500 containers and we could scale this out very easily. I guess the time reduction is pretty much linear with how many containers and EC2 instances we have.

We're about to run 2019 WOfS today, so hopefully we have similar numbers out of that!

Cheers, Alex

```
