# Use the official Python image from the Docker Hub
FROM python:3.9-slim

WORKDIR /app

RUN pip install ortools
RUN pip install --upgrade pip

COPY main.py /app/powerplant.py

ENTRYPOINT ["python", "/app/powerplant.py"]
