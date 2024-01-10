FROM ubuntu
MAINTAINER Tony Butzer
ENV REFRESHED_AT 2017-12-08

RUN apt-get -yqq update \
   &&  apt-get install -y vim

#COPY ./files/rsyslog.conf /etc/rsyslog.conf

ENV Hello Tony_1

VOLUME ["/home/tony/data"]

ENTRYPOINT ["/bin/bash"]
