echo:
	echo hi from make
	echo Please use docker compose for persistance

up:
	docker-compose up -d

down:
	docker-compose down

runr:
	docker run -it -p 8080:8888 jupyter/r-notebook jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml'

run:
	docker run -it -p 80:8888 tbutzer/jupyter-lite jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml'

bash:
	docker run -it tbutzer/jupyter-lite bash

git:
	(cd /opt/notebook; make)
