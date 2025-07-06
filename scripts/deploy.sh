#!/usr/bin/env bash
# Build and start services with docker-compose
set -e
cd infra/docker
docker-compose up --build
