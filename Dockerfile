# Use the official Python image from the Docker Hub
FROM python:3.9.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files and directories
COPY ./ ./

# Install Poetry using pip
RUN pip install --no-cache-dir poetry

# Install dependencies
RUN poetry install --with dev
