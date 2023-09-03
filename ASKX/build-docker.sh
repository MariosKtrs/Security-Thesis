#!/bin/bash
docker stop challenge
docker build --tag=challenge .
docker run -d --security-opt seccomp=unconfined -p 1337:1337 --rm --name=challenge challenge
docker exec -it challenge /bin/bash
