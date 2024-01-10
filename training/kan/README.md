# kan
hardened kanboard container

## Create SSL Cert for Nginx

- [How To Create an SSL Certificate on Nginx](https://www.digitalocean.com/community/tutorials/how-to-create-an-ssl-certificate-on-nginx-for-ubuntu-14-04)

### Synopsis

1. ./create-self-signed-cert.sh 

```
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:SouthDakota
Locality Name (eg, city) []:SiouxFalls
Organization Name (eg, company) [Internet Widgits Pty Ltd]:odcinc
Organizational Unit Name (eg, section) []:developers
Common Name (e.g. server FQDN or YOUR name) []:kan.hopto.org
Email Address []:tonybutzer@gmail.com
```


2. Register the ip with noip.com
   - onehundredworst

3. test this


## Build the kanboard container

1. clone the repo
	- cd /opt
	- git clone https://github.com/kanboard/kanboard.git

2. cp -r /opt/kanboard/docker /opt/kan/docker

3. build the container
	- cd /opt/kan/docker
	- ./build.sh

4. test the container
	- testTheContainer.sh
