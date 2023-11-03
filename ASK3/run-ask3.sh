#!/bin/sh

cd exercise3
sudo docker stop vuln_flask
sudo docker rm vuln_flask
sudo docker build -t vuln_flask .
sudo docker run --name vuln_flask -p 5050:5050 vuln_flask
