#!/bin/sh
cd server/wordpress
sudo docker stop wp
sudo docker rm wp
sudo docker build -t wp .
sudo docker run --name wp --link wp-mysql:db -p 8000:80 wp
