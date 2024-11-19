#!/bin/bash

set -e
docker-compose down

cd /app/

git pull origin master

docker-compose up -d

echo "Обновление завершено!"
