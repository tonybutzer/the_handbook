publish:
	git config --global user.email tonybutzer@gmail.com
	git config --global user.name tonybutzer
	git config --global push.default simple
	git add .
	git commit -m "automatic git update from Makefile"
	git push

up:
	(cd ./tfinfra/cubeBox; /usr/local/bin/terraform apply -auto-approve)

down:
	(cd ./tfinfra/cubeBox; /usr/local/bin/terraform destroy -force)
	(cd ./tfinfra/cubeBox; ./renameDefunct.sh)

cube:
	./credentialAWS.sh
	(cd /opt/odc; make up)
	(cd /opt/odc; make initdb)
	(cd /opt/odc; make download-pathrows-file)

index:
	./credentialAWS.sh
	(cd /opt/odc; make index)
