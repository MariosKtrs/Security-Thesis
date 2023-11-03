#!/bin/bash
docker stop cryptography
docker build --tag=cryptography .
docker run -d -p 1337:1337 --rm --name=cryptography cryptography
docker exec -it cryptography /bin/bash
