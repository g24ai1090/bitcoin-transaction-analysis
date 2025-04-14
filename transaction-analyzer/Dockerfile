FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/virtualbox-assignmnt-6d2f47e5141c.json"

EXPOSE 8080
CMD ["uvicorn", "transaction_analyzer:app", "--host", "0.0.0.0", "--port", "8080"]
