FROM ubuntu:latest

# ENV HOME /root
# ENTRYPOINT ["/bin/bash"]

ARG TARGETPLATFORM
ARG BUILDPLATFORM
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM" > /log


RUN apt-get update && apt-get upgrade -y

RUN echo " * * * * * * Installing python and pip * * * * * * "
RUN apt-get install python3 python3-pip net-tools nano -y

# RUN echo " * * * * * * Installing sqlalchemy and flask * * * * * * "
# RUN pip install sqlalchemy flask

