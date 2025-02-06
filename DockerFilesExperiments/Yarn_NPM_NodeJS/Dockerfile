FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install build-essential cmake nano curl git -y

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update
RUN apt-get install yarn  -y
RUN apt-get install nodejs npm  -y

COPY . /atc-front
WORKDIR /atc-front
