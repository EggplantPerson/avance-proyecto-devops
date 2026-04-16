FROM python:3.10 AS builder

WORKDIR /app

COPY . .

RUN pip install flask boto3

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]
