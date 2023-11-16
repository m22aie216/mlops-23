#!/bin/sh
docker build -t exp:v1 -f ./docker/Dockerfile .
docker volume create train_mod
docker run -v train_mod:/exp/models exp:v1
