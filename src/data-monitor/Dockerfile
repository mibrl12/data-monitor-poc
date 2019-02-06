FROM python:3.7.0-slim

MAINTAINER Mikalai Syty "mikalai@syty.me"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY src/ .

ENV PYTHONPATH=/app/

EXPOSE 5000
CMD ["python3", "./app.py"]
