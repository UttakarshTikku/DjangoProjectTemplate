FROM python:3.7

MAINTAINER "Uttakarsh Tikku" <github.com/UttakarshTikku>
LABEL name="Docker Build for Django Project"

# Debian Prep
# RUN apt-get clean && apt-get update -y && apt-get upgrade -y
# RUN apt-get install -y libnss3-dev fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatspi2.0-0 libgtk-3-0 libx11-xcb1 libxtst6 lsb-release xdg-utils xvfb

ENV PYTHONBUFFERED 1

RUN pip install pipenv

RUN mkdir /code
WORKDIR /code

COPY . /code

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
# RUN cd Project && python manage.py collectstatic --no-input && python manage.py makemigrations && python manage.py migrate && gunicorn --workers=BaseProject.wsgi -b 0.0.0.0:80