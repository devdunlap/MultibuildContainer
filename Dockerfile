# --- Stage 1: Build dependencies ---
FROM python:3.11-slim-bullseye AS builder

WORKDIR /app

# Update system packages to address vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install build dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
FROM python:3.11-slim-bullseye

WORKDIR /app

# Update system packages to address vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Copy wheels from builder and install
COPY --from=builder /wheels /wheels

# Copy wheels from builder and install
COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache /wheels/*

# Copy application code
COPY app ./app
COPY .env.example .env
COPY config.py .

# Expose port for Flask
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_ENV=production

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]