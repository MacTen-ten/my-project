FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "test_script.py"]FROM python:3.10-slim
WORKDIR /app
COPY . .
CMD ["python3", "test_script.py"]
