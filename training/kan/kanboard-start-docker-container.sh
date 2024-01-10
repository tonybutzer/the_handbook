sudo docker run -d -p 9999:443 \
 -v /opt/data:/var/www/app/data \
 -v /opt/plugins:/var/www/app/plugins \
 --name b_kanboard kan /bin/bash

