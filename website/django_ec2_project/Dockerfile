FROM python:3.8-slim

MAINTAINER AI Fashion <https://github.com/liemluong/Neural_Network_Art>

EXPOSE 8000

ADD . /django_ec2_project

WORKDIR /django_ec2_project

RUN apt update

#RUN apt -y install build-essential libwrap0-dev libssl-dev libc-ares-dev uuid-dev xsltproc

#RUN apt-get update -qq \
#    && apt-get install --no-install-recommends --yes \
#        build-essential \
#        gcc \
#        libgl1-mesa-glx \
#        libhdf5-dev \
#        python3-dev \
#        python3-opencv \
#        musl-dev

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

#RUN pip install --upgrade pip setuptools wheel

#RUN python -m pip install --no-cache-dir \
#      numpy scipy matplotlib scikit-build opencv-python-headless \
#      influxdb paho-mqtt configparser Pillow

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]