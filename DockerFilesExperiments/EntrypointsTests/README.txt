--progress=plain

docker build -f Dockerfile -t test_image --progress=plain .


=============================================================================
                ENTRYPOINT
=============================================================================

>  docker build -f Dockerfile_EntrypointTest -t test_image  .

# Создаем контейнер в котором запускается 'top -b'
>  docker run -it --rm --name Test1 test_image

# Что бы подключится к нему и выполнить 'ps aux'
>  docker  exec -it Test1 ps aux