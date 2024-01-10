init:
	docker run -i -t -v `pwd`/:/tfinfra tbutzer/terraform terraform init

apply:
	docker run -i -t -v `pwd`/:/tfinfra tbutzer/terraform terraform apply

destroy:
	docker run -i -t -v `pwd`/:/tfinfra tbutzer/terraform terraform destroy
	./renameDefunct.sh butzer-sship-0
	# ./renameDefunct.sh butzer-sship-1

bash:
	docker run -i -t -v `pwd`/:/tfinfra tbutzer/terraform bash

ipshow:
	terraform show |egrep  'Name|private_ip'


git:
	(cd /opt/k8s101; make)
