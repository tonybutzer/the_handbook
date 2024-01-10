#! /bin/bash -x

sudo mkdir -p /data

sudo mkdir -p /data/tar
sudo mkdir -p /data/log
sudo chmod 777 /data/log
sudo mkdir -p /data/listings
sudo mkdir -p /data/home

sudo chown -R ubuntu /data
