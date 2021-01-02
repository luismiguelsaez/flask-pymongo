FROM python:3-alpine

LABEL description="SQL database etup image"

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
ADD code/ .

RUN apk update && \
    apk add gcc musl-dev libffi-dev && \
    rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt

ENTRYPOINT ["python","/app/main.py"]