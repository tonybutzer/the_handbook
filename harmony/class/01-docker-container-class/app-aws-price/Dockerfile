FROM tbutzer/harmony-base-python

RUN mkdir -p /home/price \
    && mkdir -p /home/price/data 

COPY code /home/price
COPY price_prune.pickle /home/price
    
WORKDIR /home/price

CMD ls
