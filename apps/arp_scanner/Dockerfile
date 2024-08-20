FROM python:3-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install build-essential cmake nano git -y

COPY . /apps/arp_scanner
WORKDIR /apps/arp_scanner
