FROM python:3.7

WORKDIR /tmptmp/
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install sqlite3 libsqlite3-dev -y
RUN apt-get install -y nodejs
RUN npm install npm@latest -g
