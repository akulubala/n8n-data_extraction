FROM python:3.13.1-slim-bookworm as builder

COPY srv /srv
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl vim unzip \
    && pip install poetry==1.7.1 \
    && cd /srv/fuzzy_match \
    && poetry config virtualenvs.in-project true --local \
    && poetry install --no-root;

WORKDIR /srv/fuzzy_match

CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

