#!/bin/bash
docker stop buffer
docker build --tag=buffer .
docker run -d --security-opt seccomp=unconfined -p 1337:1337 --rm --name=buffer buffer
docker exec -it buffer /bin/bash
