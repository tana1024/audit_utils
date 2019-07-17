FROM python:3.7

CMD echo "pip start"
WORKDIR /tmptmp/
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD echo "install sqlite3 start"
RUN apt-get update
RUN apt-get install sqlite3 libsqlite3-dev -y

CMD echo "install nodejs start"
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g vue-cli
