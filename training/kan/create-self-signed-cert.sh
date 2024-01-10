#! /bin/bash -x

openssl req -new -newkey rsa:2048 -nodes -keyout hopto.key -out hopto.csr

openssl x509 -req -days 365 -in hopto.csr -signkey hopto.key -out hopto.crt
