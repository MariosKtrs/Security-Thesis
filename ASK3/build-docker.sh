#!/bin/bash
docker build --tag=challenge .
docker run --security-opt seccomp=unconfined -p 1337:1337 --rm --name=challenge challenge
