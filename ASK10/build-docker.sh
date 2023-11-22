#!/bin/bash

sudo docker stop heartbleed
sudo docker build --tag=heartbleed .
sudo docker run -d -p 1500:443 --rm --name=heartbleed heartbleed


sudo docker stop attack
sudo docker build --tag=attack attack/.
sudo docker run -d -p 5050:443 --rm --name=attack attack
sudo docker exec -it attack /bin/bash


