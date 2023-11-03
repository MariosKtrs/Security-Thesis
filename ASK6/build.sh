#!/bin/bash
sudo docker stop crypt
sudo docker rm crypt
sudo docker build --tag=crypt .
sudo docker run -d -p 1337:1337 --name=crypt crypt
sudo docker exec -it crypt /bin/bash
