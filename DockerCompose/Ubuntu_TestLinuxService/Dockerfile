FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget nano git build-essential openssh-server tcpdump net-tools sudo systemd  systemd-sysv

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

# Start SSH daemon
# CMD ["/usr/sbin/sshd", "-D"]

# enable ssh
RUN systemctl enable ssh

# systemd requires this
STOPSIGNAL SIGRTMIN+3

VOLUME ["/sys/fs/cgroup"]

CMD ["/sbin/init"]