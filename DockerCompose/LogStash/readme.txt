
docker-compose up -d  logstash

docker exec -it logstash /bin/bash


=================================================================================================================================
				  Monitoring | https://www.elastic.co/guide/en/logstash/current/monitoring-logstash.html						
=================================================================================================================================


curl -XGET 'localhost:9600/?pretty'

curl -XGET 'localhost:9600/_node/hot_threads?human=true'


=================================================================================================================================
				  Dockerfile					
=================================================================================================================================

docker build -t logstash_image .

docker run --rm -it -p 5000:5000/udp -p 9600:9600/tcp  -v /home/andtokm/Projects/Docker/DockerCompose/LogStash/conf:/home/logstash --name logstash_container logstash_image /bin/bash

# > cd /usr/share/logstash
bin/logstash -f /home/logstash/logstash.conf

# '/home/andtokm/Projects/Docker/DockerCompose/LogStash/conf' путь к каталогу с  logstash.conf

# часть настроек запуска

# apt-get install apt-transport-https
# wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | gpg --dearmor -o /usr/share/keyrings/elastic-keyring.gpg
# echo "deb [signed-by=/usr/share/keyrings/elastic-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-8.x.list
# apt-get update && apt-get install logstash

=================================================================================================================================
				 Как запустить | https://www.elastic.co/guide/en/logstash/current/first-event.html
=================================================================================================================================

cd /usr/share/logstash


> bin/logstash -e 'input { stdin { } } output { stdout {} }'
> bin/logstash -e 'input { gelf { port => 5000 } } output { stdout {} }'

# или создать файл 'logstash.conf'

input {
	gelf {
		port => 5000
	}
}

output {
	stdout {
		codec => rubydebug
	}
}

> bin/logstash -f logstash.conf


=================================================================================================================================
				 Python Log Sender App
================================================================================================================================


import datetime
import json
import socket
from typing import Dict

# LogStash server host name and port:
host, port = '192.168.101.2', 5000


def send_logs(log_data: str ) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        bytes_send: int = sock.sendto(bytes(log_data, "utf-8"), (host, port))
        print(f'{bytes_send} bytes send')


if __name__ == '__main__':

    message: Dict = {'hello': 'world'}

    data: Dict = {
        'time': str(datetime.datetime.now()),
        'level': 'Debug',
        'severity': 'Critical',
        'message': str(message).replace('\'', "\""),
        'service': 'host_metrics_app'
    }

    print(json.dumps(data))
    send_logs(json.dumps(data))

