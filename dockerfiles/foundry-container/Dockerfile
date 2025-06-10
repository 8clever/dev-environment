FROM ubuntu:22.04
RUN apt update && apt install git curl -y
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
ARG GITHUB_URL
COPY .ssh /root/.ssh
RUN chmod 400 /root/.ssh/id_rsa
RUN git clone $GITHUB_URL app
WORKDIR /app
RUN curl -L https://foundry.paradigm.xyz | bash