#!/bin/bash

set -e
docker-compose down

cd /app/

git pull origin main

docker-compose up -d
docker-compose exec app_web python manage.py migrate
docker-compose exec app_web python manage.py collectstatic
echo "Обновление завершено!"
