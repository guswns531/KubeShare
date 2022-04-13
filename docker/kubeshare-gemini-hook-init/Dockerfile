# call from repo root

# FROM nvidia/cuda:10.0-devel AS build
FROM nvidia/cuda:11.5.1-devel-ubuntu20.04 AS build

WORKDIR /tmp/build

RUN apt update && \
    apt install -y git && \
    git clone https://github.com/guswns531/Gemini.git && cd Gemini && \
    sh install.sh && \
    make -C src

# FROM busybox:1.31.1-glibc
FROM alpine:3.9

COPY --from=build /tmp/build/Gemini/lib/libgemhook.so.1 /libgemhook.so.1
COPY docker/lib/libnorm.so.1  /libnorm.so.1
COPY docker/lib/libpgm-5.2.so.0  /libpgm-5.2.so.0
COPY docker/lib/libsodium.so.23  /libsodium.so.23
COPY docker/lib/libzmq.so.5  /libzmq.so.5
COPY docker/lib/copylib.sh /copylib.sh

RUN chmod 777 /copylib.sh

CMD ["/copylib.sh"]
