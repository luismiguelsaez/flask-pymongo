FROM python:3-alpine

LABEL Description="API unit tests image"

RUN mkdir /test
WORKDIR /test
ADD code/ .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["sleep","3600"]
