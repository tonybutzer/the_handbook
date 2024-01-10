#! /bin/bash -x



ssh -i /home/ubuntu/.ssh/CHS-LSDSDPAS-butzer.pem ubuntu@`instance getip --tag=ship2` "(cd /opt/dataDog/dogTrainer; ls ;./rd2.sh)"

