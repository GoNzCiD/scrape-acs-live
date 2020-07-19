FROM python:3.8.2-alpine3.11

COPY assetto_server_scrapper /app/assetto_server_scrapper
COPY common /app/common
COPY uploaders /app/uploaders
COPY requirements.txt /app
COPY run.py /app

WORKDIR /app

RUN apk add chromium-chromedriver && pip install -r requirements.txt

CMD ["python", "run.py"]