# DOCKER TASKS
# Build the container

IMAGE=tbutzer/jup1

build: ## Build the container
	sudo docker build -t $(IMAGE) .

publish: ## Send this image to docker hub!
	sudo docker login -u tbutzer
	sudo docker push $(IMAGE)

runcan:  ## Runs the canned container from dockerhub
	docker run --rm -p 10000:8888 -e JUPYTER_LAB_ENABLE=yes -v `pwd`:/home/jovyan/work jupyter/datascience-notebook
