FROM python:3.8-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
