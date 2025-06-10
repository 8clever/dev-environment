FROM node:iron-bullseye
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
COPY .ssh /root/.ssh
RUN chmod 400 /root/.ssh/id_rsa
ARG GITHUB_URL
RUN git clone $GITHUB_URL app
WORKDIR /app