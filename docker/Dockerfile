FROM python:3.8-alpine

ENV DOCKER_ON="true"

EXPOSE 5000

COPY ./src /code

WORKDIR /code

RUN pip install .

CMD python app.py

