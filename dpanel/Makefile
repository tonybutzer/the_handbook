gitbig:
	find . -size +10M
	echo du -a ./ | sort -n -r | head -n 20
	for file in `find . -size +10M`; do ls -lh $$file; done


publish:
	git remote set-url origin git@github.com:tonybutzer/dpanel.git
	#git remote set-url origin https://github.com/tonybutzer/dpanel.git
	git config --global user.email tonybutzer@gmail.com
	git config --global user.name tonybutzer
	git config --global push.default simple
	git add .
	git commit -m "automatic git update from Makefile"
	git push

