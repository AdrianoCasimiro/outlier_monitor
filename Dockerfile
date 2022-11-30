FROM python:3.10.5

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./api /api

WORKDIR /api
EXPOSE 8000

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
