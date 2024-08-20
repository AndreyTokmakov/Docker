
docker compose down
docker compose up -d broker



# Configure SSL for RabbitMQ
# https://github.com/Nepitwin/RabbitSSL?ysclid=lodrq82kyb459126459

# Oficial manual
# https://www.rabbitmq.com/ssl.html


# https://docs.testit.software/installation-guide/set-up-external-connections/external-connection-rabbitmq.html#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D0%BA%D0%B0-%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D0%B3%D0%BE-%D1%81%D0%BE%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F


git clone git@github.com:rabbitmq/tls-gen.git
cd tls-gen/basic

make PASSWORD=12345
make verify
make info


sudo cp result/ca_certificate.pem /tmp/docker/rabbitmq/ssl/ca_certificate.pem
sudo cp result/server_AndTokmUbuntu_certificate.pem /tmp/docker/rabbitmq/ssl/server_cert.pem
sudo cp result/server_AndTokmUbuntu_key.pem /tmp/docker/rabbitmq/ssl/server_key.pem


# Docker:

docker exec -it rabbit_mq /bin/bash

# Debug
apt-get update && apt-get upgrade -y && apt-get install net-tools nano tcpdump -y

tcpdump -ne -i eth0 tcp dst port 5671 or src port 5671
