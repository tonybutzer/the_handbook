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
          mv  opendatacube-cloudformation-testing-master /opt/odc-test

          # We need write access in these places
          chmod -R 777 /opt/odc-test/notebooks
          chmod -R 777 /opt/odc-test/data
          chown -R ubuntu /opt/odc-test/data
          cd /opt/odc-test

