# personal-pangeo
for bootstrapping a personal pangeo system in AWS

# The road to Autonomy


## Logging in via ssh
- ssh ec2-user@10.12.69.13

## starting your Pangeo

- (cd opt/personal-pangeo/conda/olena; ./start_jupyter_notebook.sh)
	- could set up an alias or bash script

## connecting to the pangeo

- http://10.12.69.13:8888
	- passwd is yaml


## Starting and Stopping an Instance

- could use AWS console if you have access 
- else - pinstance - need to set this up

### Stopping the host you are ssh logged into
- sudo shutdown -h now


## building your pangeo conda

- cd opt/personal-pangeo/conda/olena
	- make build
	- pangeo_env.yml # this is a list of your python packages.

## Moving my mini-pangeo stuff
- aws cp to some bucket
- aws cp back here


## Study the repo 
- https://github.com/tonybutzer/personal-pangeo

## Build your own github repo 
- name it conda-env
	- cp personal-pangeo/conda/olena -- and -- customize it
