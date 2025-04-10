FROM python:3.12-slim as builder
LABEL authors="samuel"

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install wheel
RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels




ENTRYPOINT ["top", "-b"]