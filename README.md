# DocteurMemo Project

DocteurMemo is a Django project consisting of two applications: one for creating and managing users and another for patient prediction. The project utilizes a packaged Django app as a dependency. Additionally, there is a Docker Compose configuration included to launch the database, the two applications, and Grafana with Prometheus for monitoring.

## Project Structure

The project is organized into the following directories:

- **docteurmemo/**
  - Main Django project folder containing project-level settings.
- **docteurmemo_prediction/**
  - Django app for patient prediction.
- **docteurmemo-db-objects/**
  - Packaged Django app used as a dependency (for managing database objects).

## Getting Started

### Prerequisites

Make sure you have Docker and Docker Compose installed on your system.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/OverFlow33/docteurmemo.git
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This command will set up the database, launch the two Django applications, and start Grafana with Prometheus for monitoring.

3. Access the Django applications:

   - User Management App: [http://localhost:8000/](http://localhost:8000/)
   - Patient Prediction App: [http://localhost:8001/](http://localhost:8001/)

4. Access Grafana Dashboard:

   - [http://localhost:3000/](http://localhost:3000/)
     - Username: admin
     - Password: admin

## Project Components

### 1. User Management App

The User Management App allows for the creation and management of users. It leverages the packaged Django app for additional functionalities.

### 2. Patient Prediction App

The Patient Prediction App provides functionalities related to predicting patient outcomes. It relies on the packaged Django app and may include patient-related features.

### 3. Packaged Django App

The `django_package` directory contains a packaged Django app that serves as a dependency for both applications. This app could include reusable components, models, or utilities shared across the project.

### 4. Monitoring with Grafana and Prometheus

Grafana and Prometheus are integrated into the project for monitoring. The Grafana dashboard is accessible at [http://localhost:3000/](http://localhost:3000/). The default credentials are:

- Username: admin
- Password: admin

## Configuration

### Environment Variables

You can configure Docteurmemo by modifying environment variables in the `.env.db` and `.env` files. You need first to rename the template files `example.env.db` and `example.env` using the command :

```bash
   mv example.env.db .env.db 
   mv example.env .env 

```

Some of the key environment variables include:

#### .env.prod

- `SECRET_KEY`: Django secret key.
- `DEBUG`: Set to `True` for development and `False` for production.
- `DATABASE_URL`: URL for connecting to the PostgreSQL database.
- `DJANGO_ALLOWED_HOSTS`: Hosts or IP addresses allowed to access the Django application.
- `CSRF_TRUSTED_ORIGINS`: A list of trusted origins for unsafe requests.
- `DATABASE`, `DB_ENGINE`, `DB_USERNAME`, `DB_PORT`, `DB_PASS`, `DB_HOST`, and `DB_NAME`: PostgreSQL database configuration.

#### .env.db

- `POSTGRES_USER`: Database username.
- `POSTGRES_PASSWORD`: Database password.
- `POSTGRES_DB`: Database name.

Please make sure to update these variables for security and customization in a production environment.
