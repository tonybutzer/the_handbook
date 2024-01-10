echo 127.0.0.1 localhost >/tmp/hosts1
echo 127.0.1.1 `hostname` >>/tmp/hosts1

scp 192.168.1.100:/etc/hosts /tmp/hosts

cat /tmp/hosts1 /tmp/hosts >/tmp/newhosts

sudo cp /tmp/newhosts /etc/hosts
