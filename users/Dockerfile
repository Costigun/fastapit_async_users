FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install nano
RUN sudo apt-get install postgresql
RUN sudo apt-get install postgresql-contrib libpq-dev
RUN sudo apt-get install php5-pgsql
COPY . /app/

