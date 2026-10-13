FROM python:3.14-alpine
WORKDIR /app
COPY monitor.py .
CMD ["python", "monitor.py"]