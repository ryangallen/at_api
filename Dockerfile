FROM python:3.8

RUN apt-get update --fix-missing

WORKDIR /srv/at_api
COPY requirements.txt ./
RUN set -ex && pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

