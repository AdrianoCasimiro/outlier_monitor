FROM python:3.10.0a7-alpine3.13

WORKDIR /client
RUN mkdir /client/generated_data 

COPY client/client.py .
COPY client/generated_data/* ./generated_data/
COPY client/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000