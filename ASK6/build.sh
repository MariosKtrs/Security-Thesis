#!/bin/bash
<<<<<<< HEAD
docker stop cryptography
docker build --tag=cryptography .
docker run -d -p 1337:1337 --rm --name=cryptography cryptography
docker exec -it cryptography /bin/bash
=======
sudo docker stop crypt
sudo docker rm crypt
sudo docker build --tag=crypt .
sudo docker run -d -p 1337:1337 --name=crypt crypt
sudo docker exec -it crypt /bin/bash
>>>>>>> 14cc234fc6cc4fc80c0444bdbcd60f9d0a657c9c
