FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN pip install Django mysqlclient

COPY . .
RUN chmod +x setup.sh

CMD ["./setup.sh"]