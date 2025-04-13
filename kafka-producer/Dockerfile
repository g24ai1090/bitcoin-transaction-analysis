FROM python:3.9
WORKDIR /app
COPY kafka_producer.py requirements.txt .  
RUN pip install -r requirements.txt  
CMD ["python", "kafka_producer.py"]
