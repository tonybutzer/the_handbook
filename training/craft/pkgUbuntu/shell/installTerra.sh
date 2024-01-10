#! /bin/bash -x 
sudo apt-get install unzip
mkdir ~/opt
(
cd ~/opt
wget -O terra.zip https://releases.hashicorp.com/terraform/0.11.1/terraform_0.11.1_linux_amd64.zip?_ga=2.76081813.1069317523.1514078348-2117013944.1514078348
unzip terra.zip
sudo cp terraform /usr/local/bin
)
