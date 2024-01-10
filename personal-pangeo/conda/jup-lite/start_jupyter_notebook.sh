#!/bin/bash

IP=`hostname -I | awk '{print $1}'`
source activate olena
cd $HOME
echo ${IP}
jupyter lab --no-browser --ip=${IP} --port=8888 --NotebookApp.token='yaml'
