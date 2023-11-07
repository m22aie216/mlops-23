#!/bin/sh
docker build -t exp:v1 -f docker/Dockerfile .
docker run -it exp:v1
