# Build:

docker build -f DockerfileUbuntu -t ubuntu_gcc15_img .
docker build -f DockerfileUbuntu -t ubuntu_gcc15_img --progress=plain .

# Run:

docker run -it --rm --name gcc15_builder ubuntu_gcc15_img

=======================================================================================================================
                using multi-stage builds
=======================================================================================================================

# Build:

docker build -f DockerfileUbuntuEx -t ubuntu_gcc15_ex_img .
docker build -f DockerfileUbuntuEx -t ubuntu_gcc15_ex_img --progress=plain .

# Run:

docker run -it --rm --name gcc15_builder_ex ubuntu_gcc15_ex_img
