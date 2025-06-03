FROM python:3.11.1

WORKDIR /usr/src/app

ENV PYTHONDONTWRITENYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /urs/src/app

RUN python -m pip install gunicorn
RUN python -m pip install -U pip
RUN pip install -r requirements.txt

COPY . /usr/src/app
EXPOSE 8080