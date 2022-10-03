#syntax=docker/dockerfile:1
FROM python:latest

WORKDIR /code/

COPY requirements.txt /code/

RUN pip3 install -r requirements.txt

COPY ./app/ /code/

CMD flask --app server --debug run --host=0.0.0.0