#! /bin/bash 

echo "hello master!" >/tmp/mastergreeting.txt

sudo chown -R ubuntu /opt/dogs

./chs_install_python.sh > /tmp/pythonlang.log 2>&1
./install_python_modules.sh > /tmp/pythonmodules.log 2>&1
./initData.sh > /tmp/master.log 2>&1
./awsconfig.sh
./ersconfig.sh
./breed.sh

cp ./files/master.bashrc /home/ubuntu/.bashrc && chown ubuntu:ubuntu /home/ubuntu/.bashrc

./installServices.sh >> /tmp/master.log 2>&1


