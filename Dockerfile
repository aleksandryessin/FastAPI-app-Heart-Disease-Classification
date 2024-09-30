FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app
ENV FLASK_APP=main.py

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["bash", "./entrypoint.sh"]
