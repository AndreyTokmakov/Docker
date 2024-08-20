
docker-compose down
docker-compose up -d database



docker-compose -f docker-compose-m2.yml up -d m2_database
docker-compose -f docker-compose-m2.yml down
docker-compose -f docker-compose-m2.yml ps
