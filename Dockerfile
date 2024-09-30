# Use Python 3.11 image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Install additional applications
RUN apt update && apt install -y \
    black \
    build-essential \
    caddy \
    curl \
    entr \
    isort \
    inotify-tools \
    libffi-dev \
    libssl-dev \
    libyaml-dev \
    python3-dev \
    ripgrep \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.base.txt /tmp
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.base.txt
RUN curl -fsSL https://d2lang.com/install.sh | sh -s --
RUN curl -fsSL https://github.com/jgm/pandoc/releases/download/3.1.12.2/pandoc-3.1.12.2-1-amd64.deb -o /tmp/pandoc-amd.deb
RUN curl -fsSL https://github.com/jgm/pandoc/releases/download/3.1.12.2/pandoc-3.1.12.2-1-arm64.deb -o /tmp/pandoc-arm.deb
RUN dpkg -i /tmp/*.deb || true

CMD ["/app/bin/watch-techscreen"]
