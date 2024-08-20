docker build -t rabit_client_image .


docker run --rm -it --net=host --name rabit_client rabit_client_image /bin/bash