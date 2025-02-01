FROM python:3.13.1-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
    gcc musl-dev libffi-dev openssl-dev

WORKDIR /chat-service

COPY ./chat-service/requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/local/chat-service/start /start

RUN sed -i 's/\r//' /start && chmod +x /start