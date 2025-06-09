FROM node:iron-bullseye
COPY .ssh /root/.ssh
RUN cat /root/.ssh/id_rsa
RUN chmod 400 /root/.ssh/id_rsa
WORKDIR /app