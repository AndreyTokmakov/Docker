FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install nano wget gpg apt-transport-https net-tools -y
RUN apt-get install openjdk-17-jdk openjdk-17-jre -y

RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | gpg --dearmor -o /usr/share/keyrings/elastic-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/elastic-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-8.x.list
RUN apt-get update && apt-get install logstash -y
