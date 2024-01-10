#! /bin/bash 

List="craft dcnotebook dataHub kan ausL2 littlecube regHell ga-aws-butzer cog spag level1"

for i in $List; do echo $i ; git clone http://github.com/tonybutzer/$i; done
