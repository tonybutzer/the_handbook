info:
	echo hello cube in the box testors

up:
	docker-compose up -d

down:
	docker-compose down

exec:
	docker-compose exec debug bash

git:
	(cd /opt/notebook; make)

db-init:
	docker-compose exec jupyter datacube -v system init
	docker-compose exec jupyter datacube product add /opt/odc/docs/config_samples/dataset_types/ls_usgs.yaml

download-pathrows-file:
	wget https://landsat.usgs.gov/sites/default/files/documents/WRS2_descending.zip -O ./data/wrs2_descending.zip

index:
	# Note that you need environment variables ODC_ACCESS_KEY and ODC_SECRET_KEY set.
	# These need to be valid AWS keys. KEEP THEM SECRET, KEEP THEM SAFE!
	# need to rewrite this for usgs landsat oli-tirs albers

	echo source ~/.aws/sourceODC
	docker-compose exec jupyter bash -c \
		"cd /opt/odc/scripts && python3 ./autoIndex.py \
			-p '/opt/odc/data/wrs2_descending.zip' \
			-e '146.30,146.83,-43.54,-43.20'"
