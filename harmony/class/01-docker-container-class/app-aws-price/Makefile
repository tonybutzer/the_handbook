Image=tbutzer/aws-price

build:
	docker build -t ${Image} .

kautz:
	docker run -it --rm ${Image} python awsprice.py jkau

test:
	docker run -it --rm ${Image} python awsprice.py

run:
	docker run -it ${Image} bash

exec:
	docker exec -it ${Image} bash

dockerhub_publish:
	(docker login && docker push ${Image})

credential-hell:
	sudo apt remove golang-docker-credential-helpers
