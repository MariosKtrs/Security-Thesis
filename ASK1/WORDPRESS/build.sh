#!/bin/bash
docker stop metasploit
docker container rm metasploit
docker-compose up -d
docker build --tag=metasploit .
docker run -d -p443:443 --rm --name=metasploit metasploit
docker exec -it metasploit /bin/bash
