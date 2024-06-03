# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV POKEAPI_BASE_URL=https://pokeapi.co/api/v2

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
