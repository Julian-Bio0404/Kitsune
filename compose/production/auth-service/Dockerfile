FROM python:3.13.1-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

WORKDIR /auth-service

COPY ./auth-service/requirements /requirements
RUN pip install -r /requirements/production.txt

COPY ./compose/production/auth-service/start /start

RUN sed -i 's/\r//' /start && chmod +x /start
