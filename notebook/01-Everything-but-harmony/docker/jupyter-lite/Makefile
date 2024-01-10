Image='tbutzer/jupyter-lite'

build:
	docker build -t ${Image} .
          
push:
	docker login -u tbutzer
	docker push ${Image}

git:
	(cd /opt/notebook && make)
