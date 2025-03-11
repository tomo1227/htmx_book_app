FROM python:3.11-slim-buster
RUN apt update && export DEBIAN_FRONTEND=noninteractive \
    && apt purge -y imagemagick imagemagick-6-common
RUN pip install pipenv --no-cache-dir
