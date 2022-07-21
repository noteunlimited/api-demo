FROM python:3.8-alpine

ARG USER=notes
ARG UID=1001
ARG GID=1001

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

RUN adduser -u ${UID} --disabled-password --gecos "" ${USER} && chown -R ${USER} /app
# set to user mode
USER ${UID}:${GID}

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
