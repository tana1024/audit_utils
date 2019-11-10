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
RUN npm install -g bootstrap-vue
RUN npm install -g http-server

# 以下のinstallはローカルインストールなのでDocker起動時ではなく、個別で行うこと
#RUN npm install webpack-bundle-tracker --save-dev
#RUN npm install write-file-webpack-plugin --save-dev
#RUN npm install --save-dev node-sass sass-loader
#RUN npm install --save vue-router
#RUN npm install --save axios
#RUN npm install --save leaflet-sprite
#RUN npm install --save vue-chartjs chart.js
#RUN npm install --save vuex
#RUN npm install --save vee-validate
