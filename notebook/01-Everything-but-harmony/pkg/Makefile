cat:
	cat ./Makefile

# all: boot shared notebook cows
all: boot small fix-rasterio-curl-cert cows

boot:
	./bootstrapTheHub.sh


services:
	./installServices.sh
	./installDocker.sh


cows:
	sudo apt-get install cowsay

small:
	sudo cp ../00-Run-Me-For-Sample-Notebooks-via-git.ipynb /etc/skel

fix-rasterio-curl-cert:
	sudo mkdir -p /etc/pki/tls/certs
	sudo ln -s /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt

shared:
	sudo mkdir -p /srv/data/code
	(cd /etc/skel && sudo ln -s /srv/data/code code)
	sudo cp files/* /srv/data/code

notebook:
	(cd /srv/data/; sudo git clone http://github.com/tonybutzer/notebook)
	(cd /etc/skel && sudo ln -s /srv/data/notebook notebook)


jupyter-ubuntu:
	sudo chown -R  jupyter-ubuntu:jupyter-ubuntu /srv/data/code
	sudo chown -R  jupyter-ubuntu:jupyter-ubuntu /srv/data/notebook


ubuntu:
	sudo cp -r files /home/jupyter-ubuntu
	sudo chown jupyter-ubuntu:jupyter-ubuntu -R /home/jupyter-ubuntu


git:
	(cd /opt/notebook && make)

