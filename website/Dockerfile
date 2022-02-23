FROM python:3.6-alpine

MAINTAINER Robley Gori <ro6ley.github.io>

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /django_ec2

WORKDIR /django_ec2

RUN pip install -r requirements.txt

RUN python django_ec2_project/manage.py makemigrations

RUN python django_ec2_project/manage.py migrate

CMD [ "python", "django_ec2_project/manage.py", "runserver", "0.0.0.0:8000" ]