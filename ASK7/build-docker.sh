#!/bin/bash
sudo docker stop challenge
sudo docker rm challenge
sudo docker build --tag=challenge .
sudo docker run -d --security-opt seccomp=unconfined -p 1337:1337 --name=challenge challenge
sudo docker exec -it challenge /bin/bash
