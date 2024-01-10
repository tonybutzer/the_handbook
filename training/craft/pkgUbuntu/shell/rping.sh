#! /bin/bash -x



m1=`instance getip --tag=MasterT1`

redis-cli -h ${m1} ping

logger -p local3.info -n ${m1} "Hello from Bastion B0"


