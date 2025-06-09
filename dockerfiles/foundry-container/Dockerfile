FROM ubuntu:22.04
RUN apt update
RUN apt install git curl -y
ARG GITHUB_URL
COPY .ssh /root/.ssh
RUN chmod 400 /root/.ssh/id_rsa
RUN git clone $GITHUB_URL app
WORKDIR /app
RUN curl -L https://foundry.paradigm.xyz | bash