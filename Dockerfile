FROM python:3.8.0-alpine

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /contacts-management-flask-apis

COPY . /contacts-management-flask-apis

RUN pip3 --no-cache-dir install -r requirements.txt

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["app/docker-entrypoint.sh"]