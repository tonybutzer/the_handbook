#!/bin/bash

IP=`hostname -I | awk '{print $1}'`
#source activate steffi
echo "ssh -N -L 8888:`hostname`:8888  `whoami`@`hostname`"
cd $HOME
echo ${IP}
jupyter lab --no-browser --ip=${IP} --port=8888 --NotebookApp.token='yaml'
