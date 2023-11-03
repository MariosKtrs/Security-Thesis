#!/bin/sh

sudo docker stop ex2-phpmyadmin
sudo docker rm ex2-phpmyadmin
sudo docker build -t ex2-phpmyadmin .
sudo docker run --name ex2-phpmyadmin -p 8081:80 --link ex2-mysql:db ex2-phpmyadmin
