FROM node:iron-bullseye
ARG GITHUB_URL
COPY .ssh /root/.ssh
RUN chmod 400 /root/.ssh/id_rsa
RUN git clone $GITHUB_URL app
WORKDIR /app