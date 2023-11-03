#!/bin/sh

sudo docker stop vuln_php
sudo docker rm vuln_php
cd exercise-4
sudo docker build -t vuln_php .
sudo docker run --name vuln_php -p 8000:80 vuln_php
