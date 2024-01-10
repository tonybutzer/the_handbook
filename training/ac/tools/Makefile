AFBucket='ga-africa-provisional'
ls:
	aws s3 ls ${AFBucket}

afnuke:
	(for i in `cat africa-nuke.txt`; do echo $${i}; aws s3 rm s3://${AFBucket}/$$i; done)
	#(for i in `cat africa-nuke.txt`; do echo $${i}; aws s3 rm --recur s3://${AFBucket}/$$i; done)


Bucket='ga-odc-eros-archive-west'
gals:
	aws s3 ls ${Bucket}
nukedir:
	(for i in `cat nuke-dirs.txt`; do echo $${i}; aws s3 rm --recur s3://${Bucket}/$$i; done)
	#(for i in `cat nuke-dirs.txt`; do echo $${i}; aws s3 rm --dryrun --recur s3://${Bucket}/$$i; done)

nuke:
	(for i in `cat nuke-these-files.txt`; do echo $${i}; aws s3 rm s3://${Bucket}/$$i; done)
	#(for i in `cat nuke-these-files.txt`; do echo $${i}; aws s3 rm --dryrun s3://${Bucket}/$$i; done)


