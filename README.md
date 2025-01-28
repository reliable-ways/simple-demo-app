# Simple-demo-app

## Setup

### Prerequisites
- Python 3.11
- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/reliable-ways/simple-demo-app
    cd simple-demo-app
    ```

2. Set up the virtual environment:
    ```bash
    make setup
    ```

3. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Migrations

Run the following commands to apply the database migrations:
```bash
make migrations
```

### Running the Application

To run the application locally:
```bash
make run
```

To run the application using Docker:
```bash
make build
make run-docker
```

## Creating a Superuser

To create a superuser for the Django admin:
```bash
docker compose exec web python manage.py createsuperuser --noinput --username root --email "foo@bar.com"
```

## Running Tests

To run the tests:
```bash
docker compose exec web python manage.py test
```

## Deployment

### Building Docker Images

To build the Docker images:
```bash
docker-compose build
```

### Running Docker Containers

To run the Docker containers:
```bash
docker-compose up
```