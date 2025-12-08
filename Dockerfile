# Add proxy support if needed
# ARG HTTP_PROXY
# ARG HTTPS_PROXY

# Using Python 3.10 slim image for better compatibility
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgthread-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create necessary directories
RUN mkdir -p /data/input /data/output

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/PaddleOCR.py .

# Set environment variables
ENV INPUT_DIR=/data/input
ENV OUTPUT_DIR=/data/output

# Set the working directory to the data directory
WORKDIR /data