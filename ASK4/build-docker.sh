#!/bin/bash
docker build --tag=challenge2 .
docker run --security-opt seccomp=unconfined -p 1338:1338 --rm --name=challenge2 challenge2
