#! /bin/bash 

echo "hello master!" >/tmp/mastergreeting.txt

sudo chown -R ubuntu /opt

./initData.sh > /tmp/master.log 2>&1
./installServices.sh >> /tmp/master.log 2>&1

./installDocker.sh > /tmp/docker.log 2>&1

./awsconfig.sh
./ersconfig.sh


