FROM python:3
ENV PYTHONUNBUFFERED 1
COPY app /code/
WORKDIR /code
RUN pip install -r requirements.txt