FROM python:3.12
RUN mkdir /app_API
WORKDIR /app_API
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn appW.core:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
