#!/bin/sh
cd server/phpmyadmin
sudo docker stop wp-phpmyadmin
sudo docker rm wp-phpmyadmin
sudo docker build -t wp-phpmyadmin .
sudo docker run --name wp-phpmyadmin --link wp-mysql:db -p 8080:80 wp-phpmyadmin
