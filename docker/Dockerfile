FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYDEVD_DISABLE_FILE_VALIDATION=1

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN useradd -m analytics

USER analytics

COPY . .

ENTRYPOINT ["/bin/sh", "/app/docker/entrypoint.sh"]
