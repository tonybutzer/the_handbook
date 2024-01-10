run:
	docker run -v `pwd`:/home/jovyan -p 9998:8888 tbutzer/jupyter-lite jupyter notebook --ip 0.0.0.0 --allow-root --NotebookApp.token='yaml'


git:
	(cd /opt/notebook && make)
