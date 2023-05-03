#!/bin/bash
docker stop gobuster
docker container rm gobuster
docker stop app-container
docker container rm app-container

cd app-container/
docker build --tag=app-container .
docker run -d -p5052:80 --rm --name=app-container app-container

cd ../attack-container/
docker build --tag=gobuster .
docker run -d -p443:443 --rm --name=gobuster gobuster
docker exec -it gobuster /bin/bash

