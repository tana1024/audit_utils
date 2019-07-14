FROM python:3.7

USER ROOT

WORKDIR /tmptmp/
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN apt-get update
