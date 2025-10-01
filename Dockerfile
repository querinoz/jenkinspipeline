FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install requests
CMD ["python3", "websitecheck.py"]
