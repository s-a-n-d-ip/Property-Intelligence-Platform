FROM python:3.12-slim

WORKDIR /app

COPY requirements-lock.txt .

RUN pip install --no-cache-dir -r requirements-lock.txt

COPY app ./app
COPY artifacts ./artifacts
COPY start.sh .

RUN chmod +x start.sh 
EXPOSE 8501 8000

CMD ["./start.sh"]