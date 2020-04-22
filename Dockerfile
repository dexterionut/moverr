FROM python:3.8-alpine

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

# Installing build dependencies
RUN apk update \
    && apk add --virtual .build-deps \
    python-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN apk del .build-deps

RUN touch /var/log/cron.log

ADD crontab.txt /crontab.txt
COPY entry.sh /entry.sh
RUN chmod 755 /entry.sh
RUN /usr/bin/crontab /crontab.txt

CMD ["/entry.sh"]