#!/bin/sh

ssh -o StrictHostKeyChecking=no $HOST << 'ENDSSH'
  cd ~/ba
  docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
  docker pull $IMAGE/api:latest
  docker pull $IMAGE/frontend:latest
  docker pull $IMAGE/db:latest
  docker-compose -f devop-ci/docker-compose-prod.yml up -d --build
ENDSSH