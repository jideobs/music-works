FROM python:3.9

ENV PYTHONBUFFERED 1

COPY ./docker/django/entrypoint.sh /

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY src .
