FROM alpine:3.14

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt



EXPOSE 1234

CMD python manage.py runserver 192.168.6.3:1234
