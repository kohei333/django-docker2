FROM python:3.8
RUN apt-get update
RUN apt-get install -y postgresql
RUN apt-get install -y postgresql-contrib

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code