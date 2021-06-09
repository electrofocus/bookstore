FROM python:3.8.5

RUN apt-get update
RUN apt-get install -y netcat

WORKDIR /code

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
