FROM oven/bun:1.2-slim
RUN apt update && apt install curl -y
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
COPY .ssh /root/.ssh
RUN chmod 400 /root/.ssh/id_rsa
ARG GITHUB_URL
RUN if [[ -z "$GITHUB_URL" ]] ; then echo GITHUB_URL not provided ; else git clone $GITHUB_URL app ; fi
WORKDIR /app
