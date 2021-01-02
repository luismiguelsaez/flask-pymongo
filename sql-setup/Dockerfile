FROM python:3-alpine

LABEL description="SQL database etup image"

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
ADD code/ .

RUN pip install -r requirements.txt

ENTRYPOINT ["python","/app/main.py"]