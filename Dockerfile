FROM python:3.7

WORKDIR /tmptmp/
#COPY requirements.txt .

#RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install sqlite3 libsqlite3-dev -y
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
