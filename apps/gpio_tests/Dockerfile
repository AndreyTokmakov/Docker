FROM python:3-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install build-essential cmake nano git -y
RUN pip install RPi.GPIO

COPY . /apps/gpio_tests
WORKDIR /apps/gpio_tests
