FROM python:3.8.4-slim-buster

COPY assetto_server_scrapper /app/assetto_server_scrapper
COPY common /app/common
COPY uploaders /app/uploaders
COPY requirements.txt /app
COPY run.py /app

WORKDIR /app

RUN apt-get update && apt-get install -y chromium-driver && pip install -r requirements.txt

CMD ["python", "run.py"]