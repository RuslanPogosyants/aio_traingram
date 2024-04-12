FROM python:3.11

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

LABEL authors="r.pogosyants"

CMD ["python", "project/main.py"]
