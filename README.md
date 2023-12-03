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

## Notes

- Make sure to customize the Docker Compose configuration, such as environment variables, depending on your specific project requirements.
- For detailed information on each Django application, refer to their respective README files located in the `users` and `patient_prediction` directories.

## Contributing

If you would like to contribute to DocteurMemo, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE.md).