#! /bin/bash

echo this mounts a bucket to look like a real filesystem - sort of

sudo mkdir -p /ws-out1
sudo mkdir -p /ws-enduser1

sudo chown ec2-user:ec2-user /ws-out1
sudo chown ec2-user:ec2-user /ws-enduser1
REGION=us-west-2

sudo s3fs -o allow_other -o iam_role="butzer-ws-user-role" \
-o use_cache=/tmp \
-o url="https://s3-$REGION.amazonaws.com" \
-o umask=0227,uid=1000 \
-o nonempty     \
        ws-out /ws-out1

sudo s3fs -o allow_other -o iam_role="butzer-ws-user-role" \
-o use_cache=/tmp \
-o url="https://s3-$REGION.amazonaws.com" \
-o umask=0227,uid=1000 \
-o nonempty     \
        ws-enduser /ws-enduser1

