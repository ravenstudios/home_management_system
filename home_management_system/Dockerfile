FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ..

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

CMD ["python3", "manage.py", "makemigrations"]

CMD ["python3", "manage.py", "migrate"]

CMD ["python3", "manage.py", "createsuperuser"]
