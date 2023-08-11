From python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y wget zstd vim htop nload 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY templates ./templates
COPY scripts ./scripts

EXPOSE 8000

# --reload should be removed
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
