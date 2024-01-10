#!/bin/bash

IP=`hostname -I | awk '{print $1}'`
source activate tony
cd $HOME
echo ${IP}
jupyter lab --no-browser --ip=${IP} --port=8889 --NotebookApp.token='yaml'
