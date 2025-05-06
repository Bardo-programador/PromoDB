FROM python:3.12-slim as builder
LABEL authors="samuel"

WORKDIR /api
COPY ./requirements.txt ./requirements.txt

RUN pip install wheel
RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels


# ---------------------------------------
FROM python:3.12-slim as production

WORKDIR /api

 # Instala depedências pré-compiladas
COPY --from=builder /wheels /wheels
COPY --from=builder /api/requirements.txt /wheels/requirements.txt
RUN pip install --no-index --find-links=/wheels -r /wheels/requirements.txt


COPY ./promodb ./promodb

EXPOSE 8000

ENV PYTHONPATH=/api/projeto

CMD ["python", "promodb/manage.py", "runserver"]


