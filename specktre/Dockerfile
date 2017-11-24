FROM alpine

LABEL maintainer "Alex Chan alex@alexwlchan.net"
LABEL description "A Flask app for running Specktre, which lives at https://alexwlchan.net/tools/specktre"

RUN apk update && \
    apk add python3 py3-pillow uwsgi uwsgi-python3

COPY requirements.txt /
RUN pip3 install -r requirements.txt
