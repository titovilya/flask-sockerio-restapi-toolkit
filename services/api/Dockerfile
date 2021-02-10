FROM python:3.8.2-slim
WORKDIR /api
COPY . .
RUN apt-get update && apt-get install make
RUN python3 -m pip install -r requirements.txt
