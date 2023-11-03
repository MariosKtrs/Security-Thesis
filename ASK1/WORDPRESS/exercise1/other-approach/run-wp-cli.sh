#!/bin/sh
cd server/wp-cli
sudo docker stop wp-cli
sudo docker rm wp-cli
sudo docker build -t wp-cli .
sudo docker run -it --name wp-cli --link wp-mysql:db wp-cli
