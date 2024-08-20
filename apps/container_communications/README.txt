docker build -t receiver .
docker build -t sender .


# TODO: just run them --- не работает! контейнеры не взаимодействуют
docker run --rm -it --name receiver_container receiver /bin/bash
docker run --rm -it --name sender_container sender /bin/bash


# TODO: Так с одного контейнера можно послать сообщение на другой
docker run --rm -it --net=host --name receiver_container receiver /bin/bash
docker run --rm -it --net=host --name sender_container sender /bin/bash
