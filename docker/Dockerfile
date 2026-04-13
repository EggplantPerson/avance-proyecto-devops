FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install flask boto3

CMD ["python", "app.py"]