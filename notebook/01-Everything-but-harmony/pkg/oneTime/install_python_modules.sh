#! /bin/bash

pip3 install virtualenv

sudo mkdir /venv
sudo chown ubuntu /venv

virtualenv /venv
sudo chown -R ubuntu /venv

source /venv/bin/activate

pip3 install numpy
# pip3 install --global-option=build_ext --global-option="-I/usr/include/gdal" gdal==1.11.2
pip3 install jupyter
pip3 install shapely
pip3 install scipy
pip3 install cloudpickle
pip3 install Cython
pip3 install netcdf4
pip3 install pyproj
pip3 install requests
pip3 install rq
pip3 install awscli


(cd /opt/dataDog/instance; pip3 install -e .)

sudo chown -R ubuntu /venv

#sudo mkdir -p /opt
#(cd /opt; git clone http://github.com/tonybutzer/dataDog)
