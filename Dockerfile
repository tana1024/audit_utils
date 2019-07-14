FROM python:3.7

WORKDIR /tmptmp/
COPY requirements.txt .

RUN pip install -r requirements.txt
#RUN apt-get install --yes --force-yes sqlite3
