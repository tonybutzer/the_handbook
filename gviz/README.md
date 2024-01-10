# gviz
gaaspy viz

## Goal

- to make the USGS TE results simple to access via a set of analysis visualizations - make these browser based and dynamic.
- evaluate superset as a tool for visualizations and contrast that to python with panel

## Panel vs. Superset Tradeoffs
- panel allows complete customization
- superset has a huge open source foundation.
- superset is used and recommended by IARPA teams
- panel leverages EROS work to date

## Introduction
This repo is part of a set of python code and/or tools for visualizing test and evaluation or quality assurance work done by the USGS. We will start with relative geometric outputs (GAASPY) and use that as a model for other visualizations.

## Subprojects

### superset
### python panel apps

## Tasks Tactical

1. build bigger infrastructure for superset
2. Test docker-compose superset
	- document configurations
	- simplify
		- less examples
		- less containers
		- simplify network
3. Test full install on virgin ec2 - linux install


Issues:
1. Devops machine overwelmed no prompt at login. Possible security scann overwelm on underpowered machine.
	- WORKAROUND - - use ws aws until a bigger machine can be provisioned
	- provision a bigger machine

## Superset Technical Journey

### Docker Compose

- ref
	- https://superset.apache.org/docs/installation/installing-superset-using-docker-compose/
