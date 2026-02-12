
docker-compose up -d ubuntu24_cpp_build

docker-compose stop ubuntu24_cpp_build

docker-compose down

docker exec -it ubuntu24_cpp_build /bin/bash