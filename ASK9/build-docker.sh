#!/bin/bash
sudo docker stop buffer2
sudo docker rm buffer2
sudo docker build --tag=buffer2 .
sudo docker run -d --security-opt seccomp=unconfined -p 1337:1337 --name=buffer2 buffer2
sudo docker exec -it buffer2 /bin/bash
