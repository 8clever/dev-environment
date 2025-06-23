FROM ubuntu:22.04
RUN apt update && apt install git curl -y
WORKDIR /root/
RUN curl -L https://foundry.paradigm.xyz | bash
RUN ./.foundry/bin/foundryup
CMD ./.foundry/bin/anvil --host 0.0.0.0