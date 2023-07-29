# django-turnero

**django-turnero** is an application built using Django Rest Framework (DRF) and NextJS. It's meant for users who require a reliable and efficient reservation and shift management system. This platform enables businesses and organizations to manage their appointments, reservations, and shifts effectively.

This project was developed using the latest versions of Django, DRF, Redis, and Celery. Docker containers were utilized for easy scaling, deployment, and seamless integration with other microservices.


## Features

- Reservation Management: Users can perform essential CRUD operations (Create, Read, Update, and Delete) on reservations effortlessly.
- API:  The system was built using Django Rest Framework, the system offers a robust and RESTful API, and easily integration with other systems or applications.
- Scalable and Deployment: Benefit from the convenience of Docker containers and smooth integration with other microservices.
- Reports: Users have access to a range of valuable reports.

## Prerequisites

Make sure you have Docker installed and running. You can download Docker from the official website for your respective operating system.

## Installation

1. Environment Configuration: Create or modify the env files in the `.envs` directory. You can use the provided examples files as a template and configure the necessary environment variables.

2. Build Docker Images: Run the following command to build the Docker images:

```bash
docker-compose build
```

3. Database Setup: Once the images are built, set up the database by running the following commands:
```bash
docker-compose run django python manage.py migrate
```

4. Start the Application: Launch the application by running:

```bash
docker-compose up
```

## Configuration
To customize the project for your specific business needs, make changes to the environment variables in the .env file. This file contains crucial settings such as database configurations, and more.

### Environment variables

For configuration purposes, the following table maps environment variables to their Django setting and project settings:

| Environment Variable                  | Django Setting                 | Development Default                            | Production Default                          |
| ------------------------------------- | ------------------------------ | ---------------------------------------------- | ------------------------------------------- |
| DATABASE_URL                          | DATABASES                      |                                                | raises error                                |
| DJANGO_DEBUG                          | DEBUG                          | True                                           | False                                       |
| DJANGO_SETTINGS_MODULE                | DJANGO_SETTINGS_MODULE         | config.settings.local                          | config.settings.production                  |
| DJANGO_SECRET_KEY                     | SECRET_KEY                     | Generatearandomkey                             | raises error                                |
| DJANGO_ALLOWED_HOSTS                  | ALLOWED_HOSTS                  | localhost                                      | \*                                          |
| DJANGO_ADMIN_URL                      | ADMIN_URL                      | admin                                          | raises error                                |
| DJANGO_SECURE_SSL_REDIRECT            | SECURE_SSL_REDIRECT            | -                                              | True                                        |
| DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS | SECURE_HSTS_INCLUDE_SUBDOMAINS | -                                              | True                                        |
| DJANGO_SECURE_HSTS_PRELOAD            | SECURE_HSTS_PRELOAD            | -                                              | True                                        |
| DJANGO_SECURE_CONTENT_TYPE_NOSNIFF    | SECURE_CONTENT_TYPE_NOSNIFF    | -                                              | True                                        |
| DJANGO_EMAIL_BACKEND                  | EMAIL_BACKEND                  | django.core.mail.backends.console.EmailBackend | django.core.mail.backends.smtp.EmailBackend |
| DJANGO_DEFAULT_FROM_EMAIL             | DEFAULT_FROM_EMAIL             | -                                              |         |
| DJANGO_SERVER_EMAIL                   | SERVER_EMAIL                   | -                                              | DEFAULT_FROM_EMAIL                          |
| DJANGO_EMAIL_SUBJECT_PREFIX           | EMAIL_SUBJECT_PREFIX           | -                                              |                             |


## Contribute
We welcome contributions to enhance the capabilities of django-turnero. If you come across any issues or have ideas for improvements, feel free to open an issue or submit a pull request.