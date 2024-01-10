gitbig:
	find . -size +10M
	echo du -a ./ | sort -n -r | head -n 20
	#for file in `find . -size +10M`; do ls -lh $$file; done

fake-repo:
	(cd ..; aws s3 sync ./dinesh-repo s3://dev-et-data/logan/fakes/dinesh-repo)

examine-repo:
	aws s3 ls s3://dev-et-data/logan/fakes/dinesh-repo --recursive --human

lite:
	(cd opt; git clone http://github.com/tonybutzer/lite-stac)
