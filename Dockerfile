FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  DJANGO_ENV=develop \
  PORT=8000

RUN apt-get update && apt-get install -y --no-install-recommends \
  libpq-dev gcc \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput \
  && python manage.py makemigrations \
  && python manage.py migrate

EXPOSE $PORT

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
