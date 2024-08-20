

/usr/local/bin/docker-compose ps



/usr/local/bin/docker-compose up -d

/usr/local/bin/docker-compose down


# Что бы просто собрать:

docker-compose up --build
docker-compose build

#===============================================================================================
#                           Через  Dockerfile
#===============================================================================================

docker build -f Dockerfile -t test_image .

# Запустить контейнер так что бы он УДАЛИЛСЯ при выходе

docker run --rm -it --name test_container_name test_image /bin/bash



# Запустить контейнер так что бы он УДАЛИЛСЯ при выходе в ФОНОВОМ режиме

docker run --rm -d --name test_container_name test_image tail -f /dev/null