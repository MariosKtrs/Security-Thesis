#!/bin/bash
docker stop crypt
docker build --tag=crypt .
docker run -d -p 1337:1337 --rm --name=crypt crypt
docker exec -it crypt /bin/bash
