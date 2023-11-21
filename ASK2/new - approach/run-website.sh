#!/bin/sh

cd website
sudo docker stop ex2-website
sudo docker rm ex2-website
sudo docker build -t ex2-website .
sudo docker run --name ex2-website -p 8002:80 -p 443:443 --link ex2-mysql:db ex2-website
