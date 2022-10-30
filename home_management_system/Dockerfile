FROM python:3.8.2

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 1234

CMD python3 manage.py runserver 192.168.6.3:1234
