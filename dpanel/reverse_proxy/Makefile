Image=tbutzer/panel_demo

build:
	docker build -t ${Image} .


run:
	docker run -p 8443:5006 ${Image}


bash:
	docker run -it ${Image} sh
