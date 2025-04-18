FROM python:3.12-slim as builder
LABEL authors="samuel"

WORKDIR /app
COPY ./requirements.txt ./requirements.
COPY ./promodb/promodb_back ./promodb/promodb_back
COPY ./promodb/promodb_scrapper ./promodb/promodb_scrapper

RUN pip install wheel
RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels


