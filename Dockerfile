FROM python:3.12-slim AS builder
LABEL authors="samuel"

WORKDIR /api


# Instala o Poetry globalmente
RUN pip install --no-cache-dir poetry
RUN poetry self add poetry-plugin-export

## Instala pacotes
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
COPY ./promodb ./promodb
RUN poetry install

 # Instala dependências do sistema e remove cache de instalação
RUN poetry export -f requirements.txt --without-hashes --output requirements.txt \
 && pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels



# ---------------------------------------
FROM python:3.12-slim AS production

WORKDIR /api
COPY ./promodb ./promodb
COPY pyproject.toml poetry.lock ./


 # Instala depedências pré-compiladas
COPY --from=builder /wheels /wheels
COPY --from=builder /api/requirements.txt /wheels/requirements.txt
RUN pip install --no-index --find-links=/wheels -r /wheels/requirements.txt

# Instala raiz da api
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000

ENV PYTHONPATH=/api/promodb

CMD ["python", "promodb/manage.py", "runserver", "0.0.0.0:8000"]


