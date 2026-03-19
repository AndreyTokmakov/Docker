# Build:

docker build -f DockerfileUbuntu -t ubuntu_gcc15_img .
docker build -f DockerfileUbuntu -t ubuntu_gcc15_img --progress=plain .

# Run:

docker run -it --rm --name gcc15_builder ubuntu_gcc15_img