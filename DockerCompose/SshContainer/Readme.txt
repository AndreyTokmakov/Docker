

docker run --rm --name sshd_container -e "SSHD_USER=test" -e "SSHD_PASSWORD=test" -p 22022:22 -d testainers/sshd-container:latest

ssh root@0.0.0.0 -p22022





docker compose up -d ssh