FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  DJANGO_ENV=development

RUN apt-get update && apt-get install -y --no-install-recommends \
  libpq-dev gcc \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN cp .env.example .env \
  && ls && chmod +x .docker/setup.sh \
  && python manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT [ "./.docker/setup.sh" ]