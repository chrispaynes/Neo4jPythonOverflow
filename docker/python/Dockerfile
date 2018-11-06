FROM python:3.7.0-stretch

RUN apt-get update

WORKDIR /app

COPY ./producer/requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./producer .

CMD [ "python3", "main.py" ]
