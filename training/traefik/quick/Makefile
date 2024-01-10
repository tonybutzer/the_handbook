run:
	docker-compose up -d

down:
	docker-compose down

git:
	(cd /opt/training ; make)

test:
	curl localhost:8080/api/rawdata
	curl localhost:8080/dashboard/

