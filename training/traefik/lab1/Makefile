run:
	# docker network create proxy
	docker run -d \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v `pwd`/config/traefik.toml:/traefik.toml \
	-p 80:80 \
	-p 8080:8080 \
	-l traefik.frontend.rule=Host:monitor.example.com \
	-l traefik.port=8080 \
	--network proxy \
	--name traefik \
	traefik:1.3.6-alpine --docker 

stop:
	docker kill traefik
	docker rm traefik
git:
	(cd /opt/training; make)
