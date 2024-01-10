Image=tbutzer/sphinx
html:
	docker run\
           -v `pwd`:/home \
           ${Image} sphinx-build source build/html
	cp -r build/html/* ../docs

webServer:
	docker run --name harmony-web -p 80:80 -v `pwd`/build/html:/usr/share/nginx/html:ro -d nginx

joseWeb:
	docker run --rm --name harmony-web -p 7778:80 -v `pwd`/build/html:/usr/share/nginx/html:ro -d nginx


git:
	(cd /opt/et && make)
