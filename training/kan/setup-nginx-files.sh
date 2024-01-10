#! /bin/bash -x

mkdir -p /opt/nginx/cert
sudo chown -R ubuntu /opt/nginx

cp ./files/nginx.conf /opt/nginx
cp ./files/index.html /opt/nginx
cp ./files/hopto.* /opt/nginx/cert
