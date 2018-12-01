FROM python:3.7.0-alpine

LABEL Name=docupload

WORKDIR /app
ADD docupload/ /app
ADD ./Pipfile /app/Pipfile
ADD ./Pipfile.lock /app/Pipfile.lock

RUN python3 -m pip install pipenv
RUN pipenv install --dev --ignore-pipfile
