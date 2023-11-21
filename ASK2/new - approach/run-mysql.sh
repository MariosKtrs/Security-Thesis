#!/bin/sh

cd mysql
sudo docker stop ex2-mysql
sudo docker rm ex2-mysql
sudo docker build -t ex2-mysql .
sudo docker run --name ex2-mysql -p 3306:3306 ex2-mysql
