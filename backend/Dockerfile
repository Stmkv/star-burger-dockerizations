FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app


COPY requirements.txt requirements.txt


RUN apt update && pip install --upgrade pip && apt-get install libpq-dev -y && pip install --no-cache-dir -r requirements.txt

COPY .env /app/.env


COPY . /app
RUN python manage.py collectstatic --noinput

CMD ["python", "-m", "gunicorn", "-w","3" , "-b", "0.0.0.0:8080", "star_burger.wsgi:application"]
