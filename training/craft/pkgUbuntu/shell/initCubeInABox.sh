#/bin/bash -ex

echo "Init Cube in A Box"  2&>1 /tmp/cube.log


          # Install our dependencies
          apt-get update && apt-get -y install python-pip
          curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
          add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
          apt-get update
          apt-get install -y docker-ce python3-pip unzip wget
          pip3 install docker-compose

          # Get our code
          wget https://github.com/crc-si/opendatacube-cloudformation-testing/archive/master.zip -O /tmp/archive.zip
          unzip /tmp/archive.zip
          mv  opendatacube-cloudformation-testing-master /opt/odc

          # And get some data
          wget https://landsat.usgs.gov/sites/default/files/documents/wrs2_asc_desc.zip -O /opt/odc/data/wrs2_asc_desc.zip
          # We need to remove some local vars. This is a bit of a hack...
          sed --in-place '/AWS_/d' /opt/odc/docker-compose.yml
          sed --in-place 's/secretpassword/${SecretPassword}/g' /opt/odc/docker-compose.yml
          # another hack
          cp ./docker-compose.yml /opt/odc/docker-compose.yml
          # We need write access in these places
          chmod -R 777 /opt/odc/notebooks
          chmod -R 777 /opt/odc/data
          cd /opt/odc

