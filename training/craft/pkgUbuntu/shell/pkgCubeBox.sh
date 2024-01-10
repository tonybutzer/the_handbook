#! /bin/bash 

echo "hello master from pkgCubeBox.sh!" >/tmp/mastergreeting.txt

sudo chown -R ubuntu /opt

#./initCubeInABox.sh > /tmp/master.log 2>&1
./initCubeInABox-v2.sh > /tmp/master.log 2>&1
./dockerNonRoot.sh >> /tmp/master.log 2>&1
