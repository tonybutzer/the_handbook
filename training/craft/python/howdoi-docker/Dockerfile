FROM ubuntu:16.04
MAINTAINER Tony Butzer
ENV REFRESHED_AT 2017-11-04

RUN apt-get -yqq update \
   &&  apt-get install -y vim \
   &&  apt-get install -y python3 python3-dev python3-pip \
   &&  apt-get -y install git \
   &&  pip3 install rq \
   &&  pip3 install awscli


RUN cd /opt; git clone https://github.com/gleitz/howdoi.git \
   && cd /opt/howdoi && pip3 install -e .

