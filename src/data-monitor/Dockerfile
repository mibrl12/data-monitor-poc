FROM python:3.7.0-slim

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY src/ .

ENV PYTHONPATH=/app/

CMD ["python3", "./app.py"]
