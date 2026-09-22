FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pytest pytest-md pytest-emoji

CMD ["pytest"]
