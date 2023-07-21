From python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y wget ztsd

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

# --reload should be removed
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
