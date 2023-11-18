#!/bin/sh
docker build -t exp:v1 -f ./docker/Dockerfile .
docker volume create train_mod
docker run -d -p 80:5000 -v train_mod:/exp/models exp:v1
