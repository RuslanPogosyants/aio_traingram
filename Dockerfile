FROM python:3.11

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install poetry
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install
LABEL authors="r.pogosyants"

CMD ["python", "project/main.py"]
