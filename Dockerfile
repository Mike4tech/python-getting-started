FROM python:alpine

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80

CMD [ "python", "main.py"]
