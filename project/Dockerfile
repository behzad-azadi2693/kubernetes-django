FROM python:slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /web

COPY . /web/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ARG DJANGO_PORT
ENV DJANGO_PORT=${DJANGO_PORT}

EXPOSE ${DJANGO_PORT}

