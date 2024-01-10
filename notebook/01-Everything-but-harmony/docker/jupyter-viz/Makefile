all: jupyter-viz #push

geo-base: Dockerfile.geo
	docker build -t $@ --file $< .

geo-jupyter: Dockerfile.geo-jupyter geo-base
	docker build -t tbutzer/jupyter-geo --file $< .

Image=tbutzer/jupyter-viz
jupyter-viz: geo-jupyter
	docker build -t ${Image} .

push:
	docker login -u tbutzer
	docker push ${Image}

.PHONY: all geo-jupyter geo-base datacube-notebook
