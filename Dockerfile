FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app


RUN apt update && apt install -y g++ libpq-dev gcc musl-dev

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["./run.sh"]
