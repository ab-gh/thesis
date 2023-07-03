FROM mambaorg/micromamba:1.4.2-focal-cuda-11.7.1

USER root
RUN apt-get update && apt-get -y install sudo gcc git

ENV TZ=Europe/Zurich

COPY requirements.txt requirements.txt
COPY env.yaml env.yaml

RUN micromamba install -y -n base -f env.yaml && \
    eval "$(micromamba shell hook --shell=bash)" && \
    micromamba activate base && \
    pip install --no-cache-dir -r requirements.txt && \
    mkdir cupycache && \
    export CUPY_CACHE_DIR=./cupycache

ENV CUPY_CACHE_DIR ./cupycache