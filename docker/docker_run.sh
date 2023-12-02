#!/bin/sh
docker build -t base:latest -f ./docker/DependencyDockerfile .
docker build -t exp:latest -f ./docker/FinalDockerfile .
docker run exp:latest
