FROM python:3.8.5

RUN apt-get update
RUN apt-get install -y netcat

WORKDIR /code

COPY . .
RUN pip install -r requirements.txt
