# Build:

docker build -f Dockerfile_SeaStar -t seastar_ubuntu_img .
docker run --rm -it --net=host --name seastar_builder seastar_ubuntu_img /bin/bash