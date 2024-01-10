FROM geo-base

ENV NB_USER=jovyan \
    NB_UID=1000 \
    NB_GID=100 \
    NB_HOME=/home \
    SHELL=/bin/bash \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# Install Tini
RUN curl -s -L -O https://github.com/krallin/tini/releases/download/v0.10.0/tini && \
echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - && \
install -m 755 tini /usr/local/bin/ && rm tini

ENTRYPOINT ["tini", "--"]

# Add user
RUN useradd -s $SHELL --home-dir "${NB_HOME}" -N -u "${NB_UID}" "${NB_USER}" && \
install -d -g $NB_GID -o $NB_UID \
  $NB_HOME \
  /external/

# Notebook dependencies (download as pdf, plus misc)
RUN apt-get install -y --no-install-recommends \
      make \
      vim \
      lmodern \
      texlive-fonts-extra \
      texlive-fonts-recommended \
      texlive-generic-recommended \
      texlive-latex-base \
      texlive-latex-extra \
      texlive-xetex \
      pandoc \
      libav-tools \
      unzip && apt-get clean

RUN pip3 install --no-cache jupyterhub=='0.8.*' notebook \
    && pip3 install boto3

RUN mkdir -p /opt
WORKDIR /opt
RUN git clone https://github.com/tonybutzer/lite-stac.git \
	&& (cd /opt/lite-stac/lib && make)

ENV HOME="${NB_HOME}"
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
WORKDIR "${HOME}"
CMD ["ipython"]

ENV TONY='2.0'
COPY ./with_bootstrap /usr/local/bin/
COPY ./launch-singleuser.sh /usr/local/bin/
COPY ./launch-singleuser.sh /usr/local/bin/start-singleuser.sh
# RUN ln -s /usr/local/bin/launch-singleuser.sh /usr/local/bin/start-singleuser.sh
