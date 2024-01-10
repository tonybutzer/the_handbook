ls:
	aws s3 ls ga-africa-provisional

cp:
	aws s3 cp Makefile s3://ga-africa-provisional


grant:
	        aws s3api put-object-acl --bucket ga-africa-provisional --key Makefile --acl bucket-owner-full-control
