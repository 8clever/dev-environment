FROM ubuntu:22.04
RUN apt update && apt install git curl -y
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
RUN curl -L https://foundry.paradigm.xyz | bash
COPY .ssh /root/.ssh
RUN chmod 400 /root/.ssh/id_rsa
ARG GITHUB_URL
RUN git clone $GITHUB_URL app
WORKDIR /app
