#! /bin/bash

# sudo apt-get upadte

echo "Hello Tony" > /tmp/hellotony.txt

sudo hostname ips1
echo "127.0.0.1 ips1" >> /etc/hosts
sudo mkdir -p /opt

(cd /opt; git clone http://github.com/tonybutzer/ac)

sudo mkdir -p /data; sudo chown ubuntu /data

sudo chown -R ubuntu /opt

# (cd /opt/juphub/pkg; ./setup_os.sh)
