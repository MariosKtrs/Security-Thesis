#!/bin/bash
sudo docker stop gobuster
sudo docker container rm gobuster
sudo docker stop app-container
sudo docker container rm app-container

cd app-container/
sudo docker build --tag=app-container .
sudo docker run -d -p5052:80 --rm --name=app-container app-container

cd ../attack-container/
sudo docker build --tag=gobuster .
sudo docker run -d -p443:443 --rm --name=gobuster gobuster
sudo docker exec -it gobuster /bin/bash

