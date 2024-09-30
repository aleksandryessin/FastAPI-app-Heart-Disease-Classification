FROM public.ecr.aws/docker/library/python:3.11-slim

RUN \
    set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
    python3-pip \
    build-essential \
    python3-venv \
    ffmpeg \
    git \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip && pip3 install -U wheel && pip3 install -U setuptools==59.5.0
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt && rm -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

ENV PYTHONPATH=/app
ENV FLASK_APP=src/app.py

EXPOSE 5000

CMD ["bash", "./entrypoint.sh"]
