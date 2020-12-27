FROM python:3-alpine

LABEL Description="Simple API that allow operations against MongoDB backend"

EXPOSE 5000

RUN mkdir /app
WORKDIR /app
ADD code/ .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

ENTRYPOINT ["python","main.py"]
