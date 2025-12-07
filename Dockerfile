FROM python:3.10-slim

WORKDIR /app

# System deps for OCR
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ONLY source code
COPY PaddleOCR ./PaddleOCR

CMD ["python", "PaddleOCR/main.py"]
