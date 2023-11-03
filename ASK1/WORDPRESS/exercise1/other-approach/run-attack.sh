#!/bin/sh
cd attack-container
sudo docker stop ex1-attack
sudo docker rm ex1-attack
sudo docker build -t ex1-attack .
sudo docker run -d -p443:443 --rm --name=ex1-attack ex1-attack
sudo docker exec -it ex1-attack /bin/bash
