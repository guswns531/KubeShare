#!/bin/bash

VER=test3

docker build -t guswns531/kubeshare-config-client:$VER -f ./docker/kubeshare-config-client/Dockerfile . &&  docker push guswns531/kubeshare-config-client:$VER
docker build -t guswns531/kubeshare-gemini-hook-init:$VER -f ./docker/kubeshare-gemini-hook-init/Dockerfile . &&  docker push guswns531/kubeshare-gemini-hook-init:$VER
docker build -t guswns531/kubeshare-scheduler:$VER -f ./docker/kubeshare-scheduler/Dockerfile . &&  docker push guswns531/kubeshare-scheduler:$VER
docker build -t guswns531/kubeshare-vgpupod:$VER -f ./docker/vGPUPod/Dockerfile . &&  docker push guswns531/kubeshare-vgpupod:$VER
docker build -t guswns531/kubeshare-device-manager:$VER -f ./docker/kubeshare-device-manager/Dockerfile . &&  docker push guswns531/kubeshare-device-manager:$VER
docker build -t guswns531/kubeshare-gemini-scheduler:$VER -f ./docker/kubeshare-gemini-scheduler/Dockerfile . &&  docker push guswns531/kubeshare-gemini-scheduler:$VER


# for OBJ in kubeshare-config-client kubeshare-gemini-hook-init kubeshare-scheduler vGPUPod kubeshare-device-manager kubeshare-gemini-scheduler
# do
#     docker build -t guswns531/$OBJ:$VER -f ./docker/$OBJ/Dockerfile . &&  docker push guswns531/$OBJ:$VER
# done 
