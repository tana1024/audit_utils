FROM python:3.7

RUN pip install -r requirements.txt
RUN apt-get install -y sqlite3
