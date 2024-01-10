# Move Scene Data to S3 Buckets

* [ODC](#odc)

* [Introduction](#introduction)

* [Installation](#installation)

* [Prior Art](#prior-art)

* [Data](#data)

* [Security](#security)

* [Tools](#tools)

* [Code](#code)

    * [Python](#python)
    * [Directory Structure](#directory-structure)
    * [Git][#git]

* [Examples](#examples)

* [Acknowlegements](#acknowlegements)

* [References](#references)

* [Favorite Links](#favorite links)


# Introduction

The Open Data Cube (ODC) project is a large block of software that requires the following skill sets to setup, operate and exploit:

1. Python Software Engineer
2. EO Data Scientist
3. Project Mangment Skills
4. Linux System Administaration
5. AWS DevOps Engineer

# Document Purpose

This document describes how to run the open data cube in AWS and create a temporal/spatial datacube over Hayden Island Oregon as a test case.

# Scope, Scope, Scope

The size of the ODC technology gamut is huge, huge, huge!

A set of scoping principles is necessary to be successful with the small staff deicated to the political amnd technical landscape of ODC from the USGS.

Therefore I use the following strategtic scoping filters to narrow the focus of my work on ODC.

## Data

1. Emphasis on Landsat
    - Level 1 Collection 1
    - Surface Refelectance
        - ESPA
        - US/ARD

## Software

1. Primarily Python
2. Possibly Closure

## Infrastructure as Code

1. Primarily Terraform
2. CloudFormation - reference only

## Linux

1. Primarily Ubuntu
2. Hardened Centos for Bastion Hosts

## Project Management, System Engineering

1. Reactionary - Opportunity Based
2. Work Plan Driven
3. Strategic Plan Driven

## Cloud

1. AWS ga-aws-usgs; liberal account
2. CHS
3. Hybrid Cloud


# Document Organization

# ODC
**This section describes the ODC code exploration**

the docs are at 
[http://datacube-core.readthedocs.io/en/latest/user/intro.html](http://datacube-core.readthedocs.io/en/latest/user/intro.html)


The Data Cube is a system designed to:

-    Catalogue large amounts of Earth Observation data
-    Provide a Python based API for high performance querying and data access
-    Give scientists and other users easy ability to perform Exploratory Data Analysis
-    Allow scalable continent scale processing of the stored data
-    Track the provenance of all the contained data to allow for quality control and updates

## Website

[Website About](https://www.opendatacube.org/about)

![Why Data Cubes](../assets/whyDataCubes.png)

# Installation

## Official Documentation
Installation Instructions are HERE:

[http://datacube-core.readthedocs.io/en/latest/ops/install.html#installation](http://datacube-core.readthedocs.io/en/latest/ops/install.html#installation)


## CEOS Documentation

The CEOS documentation and code base has more real world experience to date.

### So starting here may be a good idea:
 
[ceos-seo/data_cube_ui User Interface](https://github.com/ceos-seo/data_cube_ui/blob/master/docs/datacube_install.md)

## Authors

git stats go here
notable

Because of the learning curve and the enormity of the project - people like Harshu have very few commits - it requires a black belt to commit to ODC.
Contrast that to projects like Instance, Howdoi, etc.


## AWS datacube on-demand

### cubeOD repository


[github](https://github.com/tonybutzer/cubeOD)



## Docker cube-in-a-box


### Alex G Leith

[alexgleith/docker-opendatacube](https://github.com/alexgleith/docker-opendatacube)

[magic url cloudformation](https://github.com/crc-si/opendatacube-cloudformation-testing#magic-url)

- github notes go here

## Notes from a local instance 

### on local KVM-libvirt server named bashful

**Python Version:** We use Python3 for all of our Data Cube related activities

Local user: tony

Datacube code: ~tony/Datacube

Data: /datacube/*

Viretualenv (Python 3.5?): ~/Datacube/datacube_env

Machine: odcuvm (ODC Ubuntu Virtual Machine) 
- alias = odc


### Directory Perusal

```
tony@odcuvm:~/Datacube$ ls
agdc-v2  datacube_env  data_cube_notebooks  data_cube_ui
```

#### Lines of code

```
tony@odcuvm:~/Datacube$ cloc agdc-v2/
     347 text files.
     341 unique files.                                          
     118 files ignored.

http://cloc.sourceforge.net v 1.60  T=5.72 s (47.4 files/s, 8995.4 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         151           6728           6290          21361
YAML                            96            799            155          14575
XML                              3              2              0            704
SQL                              5             24              4            235
Bourne Shell                    13             88             38            189
make                             1             30              6            145
DOS Batch                        1              8              1             28
HTML                             1              1              0              6
-------------------------------------------------------------------------------
SUM:                           271           7680           6494          37243
-------------------------------------------------------------------------------

```

#### Activate the cube python virtualenv

> alias dcenv='source ~/Datacube/datacube_env/bin/activate && python -V'



### Verify Ubuntu packages - 
### dpkg -l

[http://jon.oxer.com.au/cheatsheet/apt](http://jon.oxer.com.au/cheatsheet/apt)

```
dpkg -l postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5 libhdf5-serial-dev libnetcdf-dev libgdal1-dev hdf5-tools netcdf-bin gdal-bin


|/ Name                                 Version                 Architecture            Description
+++-====================================-=======================-=======================-=============================================================================
ii  gdal-bin                             1.11.3+dfsg-3build2     amd64                   Geospatial Data Abstraction Library - Utility programs
ii  hdf5-tools                           1.8.16+docs-4ubuntu1    amd64                   Hierarchical Data Format 5 (HDF5) - Runtime tools
ii  libgdal1-dev                         1.11.3+dfsg-3build2     all                     Geospatial Data Abstraction Library - Transitional package
ii  libhdf5-serial-dev                   1.8.16+docs-4ubuntu1    all                     transitional dummy package
ii  libnetcdf-dev                        1:4.4.0-2               amd64                   creation, access, and sharing of scientific data
ii  netcdf-bin                           1:4.4.0-2               amd64                   Programs for reading and writing NetCDF files
ii  postgresql-9.5                       9.5.8-0ubuntu0.16.04.1  amd64                   object-relational SQL database, version 9.5 server
ii  postgresql-client-9.5                9.5.8-0ubuntu0.16.04.1  amd64                   front-end programs for PostgreSQL 9.5
ii  postgresql-contrib-9.5               9.5.8-0ubuntu0.16.04.1  amd64                   additional facilities for PostgreSQL

```


and python packages

### pip list --format=columns

```
(datacube_env) tony@odcuvm:~/Datacube$ pip list --format=columns 
Package         Version             Location                   
--------------- ------------------- ---------------------------
affine          2.1.0               
cachetools      2.0.1               
click           6.7                 
click-plugins   1.0.3               
cligj           0.4.0               
cloudpickle     0.4.0               
Cython          0.27                
dask            0.15.2              
datacube        1.1.15+615.gd348e71 /home/tony/Datacube/agdc-v2
GDAL            1.11.2              
jsonschema      2.6.0               
netCDF4         1.2.9               
numpy           1.13.1              
pandas          0.20.3              
pathlib         1.0.1               
pip             9.0.1               
psycopg2        2.7.3.1             
pyparsing       2.2.0               
pyPEG2          2.15.2              
python-dateutil 2.6.1               
pytz            2017.2              
PyYAML          3.12                
rasterio        1.0a9               
scipy           0.19.1              
setuptools      36.5.0              
Shapely         1.6.1               
singledispatch  3.4.0.3             
six             1.11.0              
snuggs          1.4.1               
SQLAlchemy      1.2.0b2             
toolz           0.8.2               
wheel           0.30.0              
xarray          0.9.6               
```


### Configure the database so the following is true:

```
(datacube_env) tony@odcuvm:~/Datacube$ grep timezone /etc/postgresql/9.5/main/postgresql.conf |grep UTC
timezone = 'UTC'

sudo grep ^local /etc/postgresql/9.5/main/pg_hba.conf
local   all             postgres                                peer
local   all             all                                     md5
```

### verify postgreql service is running

```
(datacube_env) tony@odcuvm:~/Datacube$ sudo service postgresql status |grep Active
   Active: active (exited) since Sun 2017-09-24 23:11:09 CDT; 3 weeks 3 days ago


(datacube_env) tony@odcuvm:~$ more ~/.datacube.conf 
[datacube]
db_database: datacube

# db_hostname

db_username: dc_user
db_password: localuser1234
```

### Logging in to the database

#### psql -U dc_user datacube


```

Password for user dc_user: 
psql (9.5.8)
Type "help" for help.

datacube=# 
datacube=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges    
-----------+----------+----------+-------------+-------------+------------------------
 datacube  | dc_user  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/dc_user           +
           |          |          |             |             | dc_user=CTc/dc_user   +
           |          |          |             |             | agdc_admin=CTc/dc_user
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres           +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres           +
           |          |          |             |             | postgres=CTc/postgres
(4 rows)

datacube=# 
```

### Help

- \?

```
datacube-# \dt
No relations found.
datacube-# \dt *
```

## Postgresql Training Diversion

- Michael Stonebreaker - INGRESS
- PostgreSQL be at the top of your list when you start a new database-backed project?
    - Data Integrity
    - Highly Scalable
    - Feature Complete
    - On top of that, PostgreSQL also supports more than a dozen different server-side function languages, including C, SQL, PL/pgSQL, PL/Perl, PL/PHP, PL/Tcl, and PL/Ruby.


> Standards-based authentication methods, such as Kerberos, Pluggable Authentication Module (PAM), ident, and MD5 encryption, can be used to control client access to the database. This can be configured per user, per database, per connecting machine, or some combination of these, as needed for your environment. You can even require that connections be made over Secure Sockets Layer (SSL).

> Internal privileges, using standard SQL commands such as GRANT and REVOKE, allow for fine-grained control of objects inside the database. Users can be created with access to all tables, to only a few tables, or to only tables with read access. Combined with advanced features (e.g., functions, schemas, and views), you can even arrange for two different users to see completely different presentations of the same database.



Hassle-Free Licensing

PostgreSQL is licensed under a BSD license, 


Multiple Support Avenues

First and foremost, PostgreSQL has a very active and open user community. 
http://www.postgresql.org/community/lists/
http://www.postgresql.org/docs/), archived and searchable mailing lists (
http://archives.postgresql.org/), and project-hosting facilities for PostgreSQL-related software (
http://projects.postgresql.org/).


> The National Weather Service

The National Oceanic and Atmospheric Administration's (NOAA) National Weather Service (http://weather.gov) is another one of those backbone service providers that people rely on every day. 

> Downloading the Documentation

The PostgreSQL manual is available for both download and viewing via the PostgreSQL Web site (http://www.postgresql.org/docs/manuals/). Links to PDFs are available via this URL, while SGML and HTML versions are available on the PostgreSQL FTP site, at http://www.postgresql.org/ftp/.

Additionally, you can find a tremendous amount of other learning resources on the Web site http://techdocs.postgresql.org/, including a compilation of the latest tutorials from around the Web, conference papers, and information regarding matters such as PostgreSQL hosting providers, project contributors, and book reviews.


### Linux Post_installation Steps

 Step 1. Create the Postgres User

%> useradd postgres

 Step 2. Initialize the PostgreSQL Database

%> mkdir /usr/local/pgsql/data

%> chown postgres /usr/local/pgsql/data

```
sudo bash
su postgres
```

- /usr/lib/postgresql/9.5/bin/pg_ctl status
pg_ctl: no database directory specified and environment variable PGDATA unset
Try "pg_ctl --help" for more information.

To create the database use the following:

sudo -u postgres createuser --superuser dc_user
sudo -u postgres psql -c "ALTER USER dc_user WITH PASSWORD 'localuser1234';"
createdb -U dc_user datacube


#### Where is my data directory

```
SHOW data_directory;
select setting from pg_settings where name = 'data_directory';

(datacube_env) tony@odcuvm:~$ psql -U dc_user datacube
Password for user dc_user: 
psql (9.5.8)
Type "help" for help.

datacube=# show data_directory;
        data_directory        
------------------------------
 /var/lib/postgresql/9.5/main
(1 row)

```

#### IS Postgres running

- service postgresql status

or more postgres specific ...

```
(datacube_env) tony@odcuvm:~$ sudo bash
root@odcuvm:~# su postgres
postgres@odcuvm:/home/tony$ /usr/lib/postgresql/9.5/bin/pg_ctl status -D /var/lib/postgresql/9.5/main
pg_ctl: server is running (PID: 931)
/usr/lib/postgresql/9.5/bin/postgres "-D" "/var/lib/postgresql/9.5/main" "-c" "config_file=/etc/postgresql/9.5/main/postgresql.conf"

```

#### Generic template1 database 

```
root@odcuvm:~# psql -U dc_user template1
Password for user dc_user: 
psql (9.5.8)
Type "help" for help.

template1=# \l
 datacube  | dc_user  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/dc_user           +
           |          |          |             |             | dc_user=CTc/dc_user   +
           |          |          |             |             | agdc_admin=CTc/dc_user
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres           +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres           +
           |          |          |             |             | postgres=CTc/postgres

```

# Back to code


```
entry_points={
        'console_scripts': [
            'datacube-search = datacube.scripts.search_tool:cli',
            'datacube = datacube.scripts.cli_app:cli',
            'datacube-stacker = datacube_apps.stacker:main',
            'datacube-worker = datacube_apps.worker:main',
            'datacube-fixer = datacube_apps.stacker:fixer_main',
            'datacube-ncml = datacube_apps.ncml:ncml_app',
            'pixeldrill = datacube_apps.pixeldrill:main [interactive]',
            'movie_generator = datacube_apps.movie_generator:main',
            'datacube-simple-replica = datacube_apps.simple_replica:replicate'
        ]
    },
```

# datacube -v system init


- code = ~/Datacube/agdc-v2/datacube/scripts/system.py

[decorators explained](https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python)

## Click is very nuanced and complicated - used for context saving and loading in datacube

## Connecting to the database

- datacube/ui/click.py: index_connect
    - datacube/index/_api.py:connect
    - datacube/index/postgres/_apy.py 
       - PostgresDb.from_config
       - ./postgres/_connections.py:from_config -> PostgresDb.create -> LocalConfig.find
       - FINALY Return the connection index engine etc....

### Now init db

- system.py: init_db
    -  index/_api.py:init_db -< _db.init -> PostgresDb.init
    -  _connections.py:init -> ensure_db - with_permissions
        - ensure_db - creates the roles and grants for postgresql; somewhat complicated

### who creates the users?

#### list roles after init
```
datacube=# \du
                                      List of roles
  Role name  |                         Attributes                         |   Member of   
-------------+------------------------------------------------------------+---------------
 agdc_admin  | Create role, Cannot login                                  | {agdc_manage}
 agdc_ingest | Cannot login                                               | {agdc_user}
 agdc_manage | Cannot login                                               | {agdc_ingest}
 agdc_user   | Cannot login                                               | {}
 dc_user     | Superuser, Create role, Create DB                          | {}
 postgres    | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

```

### Clearing the postgresql database cluster and starting over (virgin postgres)


```
service postgresql stop
/usr/lib/postgresql/9.5/bin/initdb -D /var/lib/postgresql/9.5/main
   16  ls /var/lib/postgresql/9.5/main
   17  ls -ld /var/lib/postgresql/9.5/main
   18  sudo mv /var/lib/postgresql/9.5/main /var/lib/postgresql/9.5/main2
   19  /usr/lib/postgresql/9.5/bin/initdb -D /var/lib/postgresql/9.5/main

service postgresql start
```

### The above did not work :-( or did it :-)


or instance, to redirect all output to a file named output.sql, execute the \o command, like so:

```
corporate=> \o output.sql

ou can forego the additional typing by assigning an environment variable, like so:


corporate=> \set ap 'apressproduct'

Now it's possible to execute queries using the abbreviated name:


corporate=> SELECT name, price FROM :ap;
```

Note that a colon must prefix the variable name in order for it to be interpolated. psql also supports a number of predefined variables. A list of the most commonly used psql variables are presented in Table 27-2.

```
To view a list of all presently set variables, execute \set without passing it any parameters, like so:


corporate=> \set
```



### querying the young database after the init

```
select * from datacube.agdc.metadata_type;
select name from datacube.agdc.metadata_type;
select definition from datacube.agdc.metadata_type;
select added_by from datacube.agdc.metadata_type;
select added from datacube.agdc.metadata_type;


datacube=# \set dm datacube.agdc.metadata_type;

datacube=# select name from :dm;

```

### Running pgadmin3

### xeyes

which will let X11 forwarding server bind on the wild card address.
### $ sudo vi /etc/ssh/sshd_config
   
```
X11Forwarding yes
X11UseLocalhost no
```

pgadmin3

connect

then browse






#### END OF POSTGRES


## Python Diversion

### Code

def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.
    
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

if __name__ == "__main__":                
    print info.__doc__



[https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html)

PEP 8 Python Style Guide

## Python Style Checkers

1. flake8
2. prospector
3. pycodestyle - used to be called pep8
4. pylint


```
tony@sleepy ~ $ python
Python 3.5.4 |Anaconda custom (64-bit)| (default, Aug 14 2017, 13:26:58) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 

```

- [//docs.python.org/3/library/string.html](https://docs.python.org/3/library/string.html)



- [Argparse for CLI - Intermediate Python Programming p.3](https://www.youtube.com/watch?v=0twL6MXCLdQ)

- [list generator streams)](https://www.youtube.com/watch?v=ZoWgzG_r2qo)


## Python Packaging

* package
    - A folder/directory that contains an __init__.py file
* module
    - A file with the **.py** extension
* distribution
    - organisational construct - defines relationships in a project

### more terms you may encounter in your travels

- easy_setup
- ez_setup
- distutils
- site_packages
- egg
- pkg_resources
- wheel


setuptools replaces distutils


### setup.py 

**Links**

[Making Sense of setup.py](https://www.youtube.com/watch?v=S-Le3PWHqZA)

[Structuring Your First Python Project](https://www.youtube.com/watch?v=RKHMnevITF0&t=294s)

## Interesting Links

[sphinx](http://www.sphinx-doc.org/en/master/index.html#)

### References
[Documentation](https://readthedocs.org/)

[Flake8](https://flake8.readthedocs.org/en/latest/)

[python style talk](https://www.youtube.com/watch?v=wf-BqAjZb8M)

[Folder Structure](http://learnpythonthehardway.org/book/ex46.html)

[Licensing](http://choosealicense.com/)

[Pip](http://pip.readthedocs.org/en/stable/user_guide/)

[PyPi](https://pypi.python.org)

[reStructuredText](http://docutils.sourceforge.net/)

[Setup.py](https://docs.python.org/2/distutils/setupscript.html)

[Virtualenv](http://virtualenv.readthedocs.org/en/latest/userguide.html)

[Functional Programming](https://www.youtube.com/watch?v=oB8jN68KGcU)

## Python Debugging

[python debugger tutorial digital ocean](https://www.digitalocean.com/community/tutorials/how-to-use-the-python-debugger)

## pdb

- python3 -m pdb testhowdoi.py
    - list, l
    - breakpoint, b
    - next, n
    - step, s
    - self.failfast = True; example from unittest

## Python Case Studies

### Howdoi

[howdoi github link](https://github.com/gleitz/howdoi)

- from hitchikers
- good unittest example
- useful internet search for google, bing, stackoverflow searches
- when i get more time explore further

    
## Git

[Git Author Stats - cool](https://gist.github.com/eyecatchup/3fb7ef0c0cbdb72412fc)

[Git tutorial](https://git-scm.com/docs/gittutorial)

Tony needs to build git_tool that does these for a repo

### Tutorial

```
git --no-pager log -p |grep diff


git shortlog -sn


1131  Gregory Raevski
   959  Damien Ayers
   631  Jeremy Hooke
   320  Andrew Hicks
   222  Alex Ip
   149  Kirill Kouzoubov
    99  Peter Wang
    61  andrewdhicks
    57  woodcockr
    49  Ronnie Taib
    33  Simon Oliver
    29  simonaoliver
    26  Alex Leith
    21  Andrew Walsh
    18  Xavier Ho
    17  Imam Tashdid ul Alam
    16  Ben Lewis
    12  harshurampur
```


## Githubs of interest

Some interesting demos can be found here:
[ceos-seo jupyter notebooks](https://github.com/ceos-seo/data_cube_notebooks)

# Introduction
**This project is to move the full Scene data from the MT Hood Oregon Area to S3 Storage.

Basic steps are as follows:
- Order the data for bulk delivery via EarthExplorer
- From a rdp desktop instance in ga-aws run the BUlk Data Tool
- With a new applictaion called bulkCompanion move the data to S3 and delete the locale EBS copy immediatly
    - This code will leverage earlier ARD tile python scripts and rewrite them to be more general.

[README](http://ga-odc-eros-opt-west.s3.amazonaws.com/doc/ReadmeAbout.html)

## Data Buckets

- Full Tile h03v03 ARD (2351 Scenes)
     - [http://ga-odc-eros-ard-west.s3.amazonaws.com/AAlist.html](http://ga-odc-eros-ard-west.s3.amazonaws.com/AAlist.html)

- Cloud Free Scenes (601 Scenes)
     - [http://ga-odc-eros-opt-west.s3.amazonaws.com/AAlist.html](http://ga-odc-eros-opt-west.s3.amazonaws.com/AAlist.html)
     - [http://ga-odc-eros-opt-west.s3.amazonaws.com/h03v03/thumbs/thumbindex.html](http://ga-odc-eros-opt-west.s3.amazonaws.com/h03v03/thumbs/thumbindex.html)

- Cloud Optimized Research Set [L8, No Fill, No Clouds]
     - [http://ga-odc-eros-cog-west.s3.amazonaws.com/AAlist.html](http://ga-odc-eros-cog-west.s3.amazonaws.com/AAlist.html)
     - [http://ga-odc-eros-cog-west.s3.amazonaws.com/h03v03/thumbs/thumbindex.html](http://ga-odc-eros-cog-west.s3.amazonaws.com/h03v03/thumbs/thumbindex.html)



# Goals and Grand Problems
**This section will describe the bigger research activities associated with loading and understanding these data buckets.**

Fundamentally we want to enable scientific discovery by utillizing the "network effect"; where we place the scientist, data and tools all in the same powerful network space.

Much of this has been well articulated by folks at JPL and in this article by Chris Holmes Procuct Architect @ Planet, Board Member @ Open Geospatial Consortium on "medium.com":

- [Cloud Native Geospatial Part 1: Basic Assumptions and Workflows](https://medium.com/planet-stories/cloud-native-geospatial-part-1-basic-assumptions-and-workflows-aa67b6156b53)


The articl says:

- All data of interest to a user is in the cloud
- Infinite computation capabilities are available to process massive amounts of data
- Queuing and notification systems are in place, so newly acquired data (from satellites, from ground surveying, etc) can automatically kick off additional data processing
- Web tiled online maps are available to visualize any data (both source data and derived data 

Implications

- No Need to Duplicate Datasets
- Send Algorithms to the data, not the other way around
- The Algorithm Buffet
- Real-time GIS ; see eos.com
- Maps as verification
    - For me, it gets really interesting when the new derived data point turns into an alert that reaches a user who cares about that information.
    - static powerpoint maps replaced by fresh maps and notifications

The Future

> "Cloud Native Geospatial has the potential to introduce new, non-specialized users to the power of geospatial information that GIS practitioners have enjoyed for decades."

> "data becomes too massive to download and process locally, so users must package up their algorithms to run on the cloud. This could be a full container, like a complete Docker processing instance; but with more advanced cloud geospatial systems like RasterFoundry and Google Earth Engine a user just sends a script or a descriptions of operations to run."

[Raster Foundry by Azavea](https://www.rasterfoundry.com/)

Technical goals are as follows:

- Quickly and easily move data assets from the USGS EROS archives to the cloud.
- Package these data so as to optimize the scientists time to exploit.
- Redesign the tools to better use these new data object stores

### Expected Outcomes
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Constraints
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Approach
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Immersion
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Creating the Infrastructure
**This is where the infrastructure creation steps are documented**

In general the high level steps are as follows:

- Create ubuntu 16.04 EC2 Instance (from console) - tagged
- bullet 1
- bullet 1
- bullet 1

## Create EC2 Ubuntu Instance

- 2017-10-06 - Console - Ubuntu Server 16.04 LTS (HVM), SSD Volume Type - ami-6e1a0117
     - name tag = bulkHelper
     - Security zone and keypair are the same as bucketloader3


### Platform OS
**Ubuntu OS managment and provisioning**

- Create ubuntuUpgrade.sh in level1
- create ssh key pair and push to github
- Create loginEC2.sh $1 = instance tag
- rewrite the instance tool to handle tag names and instance id's - mulitple instance abilities


## Tools (instance)
**clone of littlecube python instance application**

### Instance
- clone this code intio level1 repo github
      - rework instance status - to handle multiple instances and ssh connection - descriptors - similar work in getip and start etc.

### Platform Provisioning
**Install xrdp and Bulk Data Tool**

### Google chrome and flash

```
chrome://settings/content

chrome://settings/content/flash
```

- enable flash 
- ask when flash is started
- then disable flash

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Platform Python
**Determine the best python venv - consider using 3.5 as ODC describes**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Repositories Utilized
**level1 and littlecube document git clone cmds here:**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Prior Art
**Discuss background and prerequisites such as ga and littlecube earlier repositories, plus key youtube references etc.**

_document reference section andmake that section well organized_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Related Work
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Study Areas
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1

## Cloud Enabled Geotiffs
## Cloud Optimized Geotif

### Why COG

1. Efficient Imagery Data Access
2. Reduced Duplication of Data
3. Legacy Compatibility (still uses geotiff)

**Growing number of data supliers using COG**

- Planet
- GDAL
- DigitalGlobe
- GeoServer
- farmshots

**Growing number of COTS developers using COG**

    - QGIS can read Cloud Optimized GeoTIFF's using Virtual Raster Builder with a vsicurl file format to refer to the online URL.
    - Marblecutter serves web tiles from Cloud Optimized GeoTIFF's, completely on the fly. You can see it in action at OpenAerialMap, as all tiles are rendered by an early version.
    - Farmshots builds agriculture analytics on top of Planet’s Cloud Optimized GeoTIFF’s, pulling in just the needed field data and serving it up live to their customers.
    - DigitalGlobe has built a project called IDAHO that can read COG files and perform on the fly band math analysis.
    - GeoServer can use a new GeoTools community module named 's3-geotiff' to use COG's as a datastore. Advanced GeoServer users who know how to add new datastores can find it in the Boundless nightly repo (use the s3:// url form for it to work).
    - Earth Observing System’s Engine and Land Viewer are both able to leverage Cloud Optimized GeoTIFFs for live web tile serving and on the fly band math.
    - GeoTrellis has not yet implemented, but has detailed their plans to do so.


### How COG (code examples)

Here is the code that Planet Labs uses to download and store the data on AWS: 

- [landsat ingestor](https://github.com/landsat-pds/landsat_ingestor)

[Jed's Javascript s3 browser](https://s3-us-west-2.amazonaws.com/landsat-pds/index.html)

Notes on the compression we use: 

- [compression notes](https://github.com/landsat-pds/landsat_ingestor/blob/master/Compression.md)

The line that does the internal tiling via GDAL: 

- [GDAL COG Generation](https://github.com/landsat-pds/landsat_ingestor/blob/837606f9635dcc73b50566598e4b92c963151b80/ingestor/splitter.py#L19)


### COG References

- [//www.cogeo.org](http://www.cogeo.org)

- [//trac.osgeo.org/gdal/wiki/CloudOptimizedGeoTIFF](https://trac.osgeo.org/gdal/wiki/CloudOptimizedGeoTIFF)



## S3

![S3 naming Optimization](./assets/s3ObjectNaming.png)

# Data
**LANDSAT Scene and ARD Data**

## ARD
[https://landsat.usgs.gov/ard](https://landsat.usgs.gov/ard)

### Grid Map

[https://landsat.usgs.gov/sites/default/files/images/CONUS_ARD_LMWS.jpg](https://landsat.usgs.gov/sites/default/files/images/CONUS_ARD_LMWS.jpg)

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1

### Realated Work Scene Data

[https://landsatonaws.com/](https://landsatonaws.com/)

[https://aws.amazon.com/public-datasets/landsat/](https://aws.amazon.com/public-datasets/landsat/)


The github repo for building the landsat-pds is

[https://github.com/landsat-pds/landsat_ingestor](https://github.com/landsat-pds/landsat_ingestor)

This code base has python for:
1. ingetsing landsat scenes
2. creating simple directory indesxes with thumbnails and quasi browse
3. pareser for taking landsat mtl.txt metadata and pasing backa pyhton dict
4. 

[Landsat Viewer - way cool](https://lv.eosda.com/?lat=43.32193&lng=-99.01909&z=11&s=Landsat8&b=NIR,Red,Green&id=LC08_L1TP_031029_20170907_20170926_01_T1)

> Not as cool - but current and useful mapbox

[https://www.mapbox.com/bites/00145/#10/45.7095/-122.9597](https://www.mapbox.com/bites/00145/#10/45.7095/-122.9597)

[https://landsat-pds.s3.amazonaws.com/c1/L8/139/045/LC08_L1TP_139045_20170304_20170316_01_T1/index.html](https://landsat-pds.s3.amazonaws.com/c1/L8/139/045/LC08_L1TP_139045_20170304_20170316_01_T1/index.html)

[example browse](http://landsat-pds.s3.amazonaws.com/c1/L8/046/028/LC08_L1TP_046028_20170730_20170801_01_RT/LC08_L1TP_046028_20170730_20170801_01_RT_thumb_large.jpg)


aws ls --recursive landsat-pds/c1/L8/046/028


 1132  aws s3 cp s3://landsat-pds/c1/L8/046/028/LC08_L1GT_046028_20170511_20170512_01_RT/LC08_L1GT_046028_20170511_20170512_01_RT_MTL.txt ~


### Download Methodology Steps
**Details of how the data was loaded - in this case level1 data**

This data was prepared doing the following steps:

- Search for level1 data (over Mount Hood, Oregon, USA) using:
    - EarthExplorer; excellent data discover tool by the USGS.
    - Landsat Look Viewer - investigate in more simple ways the scenes and their full resolution browse.; also an execellent mapping tool for undestanding and Area of Interest versus Landsat WRS coverage.
- Download the bulk scenes usin the java based Bulk Data Download Tool
- Move these to s3 with custom python code - bulkmv moves3
    - wrap this in a loop as such `for i in {1..100}; echo $i; bulkmv moves3; sleep 60; done`
- Provide AAlist.html file for web based directory of this bucket

Next steps are to look at lambda service to untar this data ad prepare it for cloud exploitation
- bullet 1
- bullet 1


## GIS
**This should probably be a main topic**

### Coordinate Reference Systems and Map Projections

#### Many Options

- State Plane
- Lat/Longe (WGS 84)
- Web Mercator/Google Mercator
- Irish National Grid
- British National Grid
- BC Albers
- Universal Transverse Mercator
- EASE Grid
- World Geographic Reference System


Why not just use Lat Long?

- because its not so great for mesauring distances and/or representing data in 2d maps
    - Geodesic distance instead of straight line distance

Common one used for directions is Web Mercator or Google Metrcator - not so great for area measures however


### EPSG - European Petroleum Survey Group 

Structured dataset of Coordinate Reference Systems

> The primary EPSG Dataset is maintained in the online registry, from which data may be accessed through a graphic user interface or through a service interface. The online registry contains the most current data. Registry users may query and view the data, generate printable reports and create Well-known Text (WKT) compliant with ISO 19162.

- [http://www.epsg.org/](http://www.epsg.org/)



EPSG 4326 = lat long wgs84
ESPG 900913 - google spherical mercator

SpatialReference.org

[http://spatialreference.org/](http://spatialreference.org/)

### Example Metadata

[http://www.epsg-registry.org/export.htm?wkt=urn:ogc:def:crs:EPSG::6579](http://www.epsg-registry.org/export.htm?wkt=urn:ogc:def:crs:EPSG::6579)

```
PROJCRS["NAD83(2011) / Texas Centric Albers Equal Area",
  BASEGEODCRS["NAD83(2011)",
    DATUM["NAD83 (National Spatial Reference System 2011)",
      ELLIPSOID["GRS 1980",6378137,298.257222101,LENGTHUNIT["metre",1.0]]]],
  CONVERSION["Texas Centric Albers Equal Area",
    METHOD["Albers Equal Area",ID["EPSG",9822]],
    PARAMETER["Latitude of false origin",18,ANGLEUNIT["degree",0.01745329252]],
    PARAMETER["Longitude of false origin",-100,ANGLEUNIT["degree",0.01745329252]],
    PARAMETER["Latitude of 1st standard parallel",27.5,ANGLEUNIT["degree",0.01745329252]],
    PARAMETER["Latitude of 2nd standard parallel",35,ANGLEUNIT["degree",0.01745329252]],
    PARAMETER["Easting at false origin",1500000,LENGTHUNIT["metre",1.0]],
    PARAMETER["Northing at false origin",6000000,LENGTHUNIT["metre",1.0]]],
  CS[cartesian,2],
    AXIS["easting (X)",east,ORDER[1]],
    AXIS["northing (Y)",north,ORDER[2]],
    LENGTHUNIT["metre",1.0],
  ID["EPSG",6579]]
```


[https://en.wikipedia.org/wiki/Albers_projection](https://en.wikipedia.org/wiki/Albers_projection)

[https://en.wikipedia.org/wiki/List_of_map_projections](https://en.wikipedia.org/wiki/List_of_map_projections)

# PROJECTION ANIMATION
[jasondavies](http://www.jasondavies.com/maps/transition/)


## Projections in Python

### Proj.4 (Cartographic Projections Library)

- originally written by Garald Evenden then of the USGS (C++)
    - now Maintained and copywright Frank Warmerdam
- Comprehensive list of existing projectsions and tool for transformation

- Open Source Geospatial Foundation (OSgeo) project


### PyProj (Python interface to Proj.4)

- supports Python buffer protocol - regular arrays and numpy arrays
- crtographic transformations and geodetic computations
- Cython wrapper to provide interfaces to PROJ.4
- MIT Licenced


many of the libraries are founded by osgeo (your open source compass)

[http://www.osgeo.org/](http://www.osgeo.org/)


```
OSGeo Projects
Content Management Systems

    GeoNode

Desktop Applications

    GRASS GIS
    gvSIG
    Marble
    QGIS

Geospatial Libraries

    FDO
    GDAL/OGR
    GEOS
    GeoTools
    Orfeo ToolBox (OTB)
    OSSIM
    PostGIS

Metadata Catalogs

    GeoNetwork
    pycsw

Web Mapping

    deegree
    geomajas
    GeoMOOSE
    GeoServer
    Mapbender
    MapFish
    MapGuide Open Source
    MapServer
    OpenLayers
```


#### simple code example python reproject

```
from pyproj import Proj

# Create projection transformation object

p = Proj(init='epsg:3857'`)  # EPSG code for Web Mercator - would 900913 give the same result?

# Convert from long/lat to Marcator and Back

print(p(-97.740372, 30.282642))

```

- git clone https://github.com/carsonfarmer/python_geospatial.git
    - loaded on sleepy in ~/learn


# LEFT OFF HERE at 37:22 in the video
[Geospatial data in Python: Database, Desktop and the Web - Part 1 | SciPy 2014 | Carson Farmer](https://www.youtube.com/watch?v=ctdjAir4TUg&list=PL16QizNnMFGd64BIRhbe6t86sgv4MvOdI)

-body-

## GDAL

# NEED to Practice with this tutorial and related references

- [gdal part 4 - medium.com](https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-4-working-with-satellite-data-d3835b5e2971)

 typical workflow to create an image from raw satellite data would be:

    Download data.
    Re-order or assemble bands into the desired order (red, green, blue; or near-infrared, red, green; etc.)
    Increase the resolution with pan-sharpening, if desired.
    Contrast-stretch and color-correct the imagery, either algorithmically or by hand.
    Restore georeferencing information, if necessary.
    Crop, re-project, and re-size image to merge with other data.


### Wavelengths and Band conventions:

[Why is that Forest Red and that Cloud Blue?](https://earthobservatory.nasa.gov/Features/FalseColor/)

1. That’s because they’re ordered from short (blue) to long (infrared) wavelengths.
    - although there are exceptions (*cough* Landsat 4, 5, & 7 *cough*).

```
gdal_translate 1155205_2017-03-31_RE3_3A.tif 1155205_2017-03-31_RE3_3A_rgb.tif -b 3 -b 2 -b 1 -co COMPRESS=DEFLATE -co PHOTOMETRIC=RGB
```

> Adding the option -b 3 -b 2 -b 1 assigns band 3 to blue, band 2 to green, and band 3 to red. -co COMPRESS=DEFLATE enables an efficient lossless compression scheme to keep the file size from getting outrageous, and -co PHOTOMETRIC=RGB ensures any image viewer will display the bands as red, green, blue (instead of an alpha channel or something).


#### Getting the min and max

> Do we need to stretch this image?

```
gdalinfo -mm 1155205_2017-03-31_RE3_3A_rgb.tif
```

Algorithmic Image Enhancement

Since our eyes sense light proportionally, the data still need to be stretched to compensate, despite filling most of the available range. Like so:

```
gdal_translate 1155205_2017-03-31_RE3_3A_rgb.tif 1155205_2017–03–31_RE3_3A_rgb_scaled.tif -scale 1422 49572 0 65535 -exponent 0.5 -co COMPRESS=DEFLATE -co PHOTOMETRIC=RGB

```

> This does two important things. -scale 1422 49572 0 65535 stretches each band equally from from a range of 1,422–49,572 (first pair of numbers) to a range of 0–65,535 (second pair of numbers). I could have scaled each band separately to its extents (which is an extremely common image processing technique) but that would likely engender a hue shift. Equal scaling leaves things looking more natural. -exponent 0.5 raises each band to the power of ½—the square root. It’s a quick and dirty way to get a preview image.


#### Color Correctionis a vast topic:

Color correction of satellite imagery is a vast topic. I’ve written two guides, one with Landsat 8 and one with PlanetScope data—they’re the process for both works fairly well for 

- [https://earthobservatory.nasa.gov/blogs/elegantfigures/2013/10/22/how-to-make-a-true-color-landsat-8-image/](https://earthobservatory.nasa.gov/blogs/elegantfigures/2013/10/22/how-to-make-a-true-color-landsat-8-image/)

- [https://www.planet.com/pulse/color-correction/](https://www.planet.com/pulse/color-correction/)

- [Landsat 8 Photoshop Tutorial](http://www.shadedrelief.com/landsat8/introduction.html)

- [Processing Landsat 8 Imagery](https://tilemill-project.github.io/tilemill/docs/guides/landsat-8-imagery/)

## Lat Long Converters

[http://www.rapidtables.com/convert/number/degrees-minutes-seconds-to-degrees.htm](http://www.rapidtables.com/convert/number/degrees-minutes-seconds-to-degrees.htm)

[lat long to placename](https://www.latlong.net/Show-Latitude-Longitude.html)


## Links

   - How to build the virtual raster for a Landsat 8 image in QGIS
   - [link](https://www.youtube.com/watch?v=YofH7eFTnNA)


- [webmapping presentation](https://docs.google.com/presentation/d/1_uKx_haEOecKzT6JKcPSZ3XA9M6PYiavfWbXPQS8ZvE/edit#slide=id.gbc1309387_0_445)
- [webmapping video](https://www.youtube.com/watch?v=MA0AqcT5qbs&t=2209)
- bullet 1
- bullet 1


## GIS

   - [Python Programming and GIS](https://www.youtube.com/watch?v=F1_FqvbXHb4)
   - [Using Geospatial Data with Python, SciPy2013 Tutorial, Part 1 of 6](https://www.youtube.com/watch?v=1fzQKMp_tdE&list=PLU7fmFhYyOzk5kTnr4pA01YvJv52--vUq)

   - Geospatial data in Python: Database, Desktop and the Web - Part 1 | SciPy 2014 | Carson Farmer

   - [** Geospatial data in Python: Database, Desktop and the Web - Part 1](https://www.youtube.com/watch?v=ctdjAir4TUg&list=PL16QizNnMFGd64BIRhbe6t86sgv4MvOdI)

   -   maybe this one
          - [Introduction to Python GIS for Data Science](https://www.youtube.com/watch?v=2u-KFbRX44I&t=870s)


## Python


### XML

[Python XML Jumpstart in only 5 minutes](https://www.youtube.com/watch?v=rFxXDO8-keg)

[Parsing XML Files in Python](https://www.youtube.com/watch?v=c2qlCZhkwtE&list=PL258FD4D8488586FA)



### EarthExplorer
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Automation Employed
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Automation Dream aka Wishlist
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Security
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Lessons Learned
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Tools
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### gitpush.sh
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### instance
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### readmeBuilder
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### git
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Code
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Python
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


### Directory Structure
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Examples
**topic sentence bold**

_body_

-body-

- bullet 1
- bullet 1
- bullet 1
- bullet 1


# Acknowlegements
**topic sentence bold**

_body_

-body-

- [http://jonschlinkert.github.io/remarkable/demo/](http://jonschlinkert.github.io/remarkable/demo/)
- bullet 1
- bullet 1
- bullet 1

# References

## Data Buckets

[Data Buckets Readme](http://ga-odc-eros-opt-west.s3.amazonaws.com/doc/ReadmeAbout.html)

## Aws Batch

Part of the agreement that AWS is making with the government is to use AWS Batch. Here are some references I've put together.

### AWS Batch Reference

[How AWS Batch Works 1 link](https://www.youtube.com/watch?v=T4aAWrGHmxQ)

[https://aws.amazon.com/batch/ documentation 2 link](https://aws.amazon.com/batch/)

### re:Invent 2016 Batch Announcement

[Batch Announcement 2016](https://www.youtube.com/watch?v=ebwfhSS4ZkY)

### Immutable Infrastucture
[AWS re:Invent 2016: Life Without SSH: Immutable Infrastructure in Production ](https://www.youtube.com/watch?time_continue=377&v=fEuN5LkXfZk)

> Brian will be working with this team to get the Weakness Verification forms completed.

### Misc Links

[Mind Maps](https://app.mindmup.com/map/new/1507293301558#)

A utility to search, download and process Landsat 8 satellite imagery
[landsat-utils](https://github.com/developmentseed/landsat-util)

### S3 Links

[request-rate-perf-considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)


# Software Licenses

[Software Licenses Explained](https://medium.freecodecamp.org/how-open-source-licenses-work-and-how-to-add-them-to-your-projects-34310c3cf94)

## Favorite Links

[https://earthobservatory.nasa.gov/blogs/elegantfigures/2013/10/22/how-to-make-a-true-color-landsat-8-image/](https://earthobservatory.nasa.gov/blogs/elegantfigures/2013/10/22/how-to-make-a-true-color-landsat-8-image/)


[A Gentle Introduction to GDAL Part 4: Working with Satellite Data](https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-4-working-with-satellite-data-d3835b5e2971)
