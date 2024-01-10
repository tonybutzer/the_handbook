hi:
	echo hi

status:
	(export PROJ_LIB=/opt/tljh/user/share/proj; datacube --version)

init:
	(export PROJ_LIB=/opt/tljh/user/share/proj; datacube -v system init)


testdb:
	echo \dt '*.*' look for agdc
	psql -U opendatacube -h localhost opendatacube 


download-index:
	(cd ~/opt ;git clone http://github.com/tonybutzer/indexc2)
