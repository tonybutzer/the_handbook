# Tools for analyzing python code source files and dependency relationships

## pyan, dependency-graph

### pyan is my favorite so far


# pyan

> Pyan is nice for looking at a single source file and/o multipl source files. Well designed code and extraneous code can be easilt spotted.

## Eample 

```
pyan /opt/dogs2/dataDog/dataDog/dogapi.py | dot -Tsvg -o dogapi.svg

pyan /opt/dogs2/dataDog/dataDog/dogapi.py | grep -v EarthExplorer | dot -Tsvg -o dogapi.svg
```

- svg files can be easily edited in inkscape
	- triple click to chane color to yello
	- move around nodes and lines - delete others


## Install as

- pip install -e . 
	- uses python 2
	
## Features

- dot files are cool

## newer more complicated versions

see this https://stackoverflow.com/questions/13963321/build-a-call-graph-in-python-including-modules-and-functions

---

# dependency-graph

## README.md
# from this package

https://gist.github.com/jbgo/1123577

```
python3 dependency-graph.py datacube | dot -Tpng -o datacube-dependencies.png
```

normal text

---

## pycallgraph

- very compicated - likely really cool - but hard to use and comprehend - maybe someday
