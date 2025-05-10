FROM python:3.11-alpine

WORKDIR /app

COPY fetch_metadata.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "fetch_metadata.py"]
