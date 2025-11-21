FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .

# create persistent directory for state
VOLUME ["/app"]

CMD ["python", "bot.py"]
