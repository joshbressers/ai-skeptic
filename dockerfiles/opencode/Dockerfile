FROM debian:latest

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get update && apt-get -y install curl virtualenv

RUN useradd -m -s /bin/bash opencode
USER opencode

RUN curl -fsSL https://opencode.ai/install | bash
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN mkdir -p /home/opencode/.config/opencode
COPY opencode.jsonc /home/opencode/.config/opencode/

WORKDIR /home/opencode/
CMD ["/bin/bash", "-l"]
