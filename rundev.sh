#!/usr/bin/env bash
docker build -t myblog:dev -f Dockerfile .
docker run --rm -p 8002:8000 --name myblog-dev --mount type=volume,src=myblog-db,target=/opt/data/ myblog:dev python3 ./manage.py runserver 0.0.0.0:8000