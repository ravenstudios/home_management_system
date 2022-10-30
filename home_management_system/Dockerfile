#  Home Management System Dockerfile
FROM python:3.9


ENV PYTHONUNBUFFERED 1

RUN mkdir /hms
WORKDIR /hms
COPY . /hms/
COPY requirements.txt /hms/requirements.txt


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


EXPOSE 1234

CMD docker-compose up
# CMD python manage.py runserver 0.0.0.0:1234
