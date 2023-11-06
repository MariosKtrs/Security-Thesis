#!/bin/bash

sudo docker stop cryptography
sudo docker build --tag=cryptography .
sudo docker run -d -p 1337:1337 --rm --name=cryptography cryptography
sudo docker exec -it cryptography /bin/bash


