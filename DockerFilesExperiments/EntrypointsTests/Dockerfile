FROM python:3-slim

RUN apt-get update && apt-get upgrade -y
# RUN pip install sqlalchemy flask

COPY app /app
WORKDIR /app

# Set code to run at container run time
ENTRYPOINT ["python", "/app/main.py"]