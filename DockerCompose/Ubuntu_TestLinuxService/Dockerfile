FROM ubuntu:latest

# Update system and install packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
        wget \
        nano \
        git \
        build-essential \
        openssh-server \
        tcpdump \
        net-tools \
        sudo \
        systemd \
        systemd-sysv \
        nginx
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Create SSH run directory
RUN mkdir /var/run/sshd

# Create user (change username/password as needed)
ARG USERNAME=test
ARG PASSWORD=test

RUN useradd -m -s /bin/bash ${USERNAME} \
    && echo "${USERNAME}:${PASSWORD}" | chpasswd \
    && usermod -aG sudo ${USERNAME}

# Optional: allow password authentication
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Enable services in systemd
RUN systemctl enable ssh
RUN systemctl enable nginx

# systemd requirements
# STOPSIGNAL SIGRTMIN+3
VOLUME ["/sys/fs/cgroup"]

VOLUME ["/sys/fs/cgroup"]

CMD ["/sbin/init"]