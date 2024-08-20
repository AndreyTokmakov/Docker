docker network create mongoCluster
docker-compose up -d mongo_node_1
docker-compose up -d mongo_node_2
docker-compose up -d mongo_node_3