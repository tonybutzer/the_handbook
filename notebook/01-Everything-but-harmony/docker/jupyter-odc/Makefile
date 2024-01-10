all: datacube-notebook

geo-base: Dockerfile.geo
	docker build -t $@ --file $< .

geo-jupyter: Dockerfile.geo-jupyter geo-base
	docker build -t $@ --file $< .

datacube-notebook: Dockerfile.datacube geo-jupyter
	docker build -t $@ --file $< .


jupyter-odc:
	docker build -t tbutzer/jupyter-odc --file Dockerfile.datacube .


push:
	docker login -u tbutzer
	docker push tbutzer/jupyter-odc

.PHONY: all geo-jupyter geo-base datacube-notebook
