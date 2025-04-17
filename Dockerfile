FROM python:3.12-slim as builder
LABEL authors="samuel"

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install wheel
RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels



FROM node:23.10-slim as prod
COPY . .

RUN npm install ./promodb_front
ENTRYPOINT ["top", "-b"]