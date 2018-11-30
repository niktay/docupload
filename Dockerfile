FROM python:3.7.0-alpine

LABEL Name=docupload
EXPOSE 80

WORKDIR /app
ADD docupload/ /app
ADD ./Pipfile /app/Pipfile
ADD ./Pipfile.lock /app/Pipfile.lock

RUN python3 -m pip install pipenv
RUN pipenv install --ignore-pipfile
CMD ["pipenv", "run", "python3", "-u", "manage.py", "runserver", "0.0.0.0:80"]