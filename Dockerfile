FROM python:3.8-slim-buster

RUN apt-get update

ENV PYTHONUNBUFFERED 1
WORKDIR /auth-app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8008
COPY . .