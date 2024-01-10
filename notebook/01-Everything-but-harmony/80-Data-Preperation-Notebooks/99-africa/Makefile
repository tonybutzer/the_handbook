
#--volume -> Bind mount a volume. The --volume flag mounts the current working directory into the container
#--publish -> Publish a container’s port(s) to the host (in my case, I used the ephemeral port 5000 as host's endpoint.)
butz:
	docker run --volume `pwd`:/home --publish 9999:8888 tbutzer/notebook jupyter-notebook --ip 0.0.0.0 --allow-root --NotebookApp.token=''
