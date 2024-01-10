
nonessus:
	docker run -it -v `pwd`:/home/jovyan -p 8888:8888 pangeo/pangeo-notebook jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml'
pangeo:
	docker run -it -v `pwd`:/home/jovyan -p 8443:8888 pangeo/pangeo-notebook jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml'
