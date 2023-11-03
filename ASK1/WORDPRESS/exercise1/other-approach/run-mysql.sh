#!/bin/sh
cd server/mysql/
sudo docker stop wp-mysql
sudo docker rm wp-mysql
sudo docker build -t wp-mysql . 
sudo docker run --name wp-mysql wp-mysql

