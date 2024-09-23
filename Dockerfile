FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFEERED 1

RUN apt-get update && \
    apt install -y python3-dev

RUN pip install --upgrade pip
RUN pip install poetry

# Создание рабочей директории
RUN mkdir /chat

# Установка рабочей директории
WORKDIR /chat

# Копирование файлов
COPY pyproject.toml poetry.lock /chat/
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

# Копирование остального кода
COPY . .
