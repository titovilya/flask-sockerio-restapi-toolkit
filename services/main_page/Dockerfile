FROM python:3.8.2-slim
WORKDIR /main_page
ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true
COPY . .
RUN python3 -m pip install -r requirements.txt