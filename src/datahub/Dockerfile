FROM python:3.7.0-slim

MAINTAINER Mikalai Syty "mikalai@syty.me"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY src/ .

ENV PYTHONPATH=/app/

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--log-level", "INFO"]
CMD ["app:app"]
