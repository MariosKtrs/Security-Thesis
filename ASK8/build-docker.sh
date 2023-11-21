#!/bin/bash

sudo docker stop crypt2
sudo docker build --tag=crypt2 .
sudo docker run -d -p 1337:1337 --rm --name=crypt2 crypt2
sudo docker exec -it crypt2 /bin/bash


