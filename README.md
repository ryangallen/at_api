# Adventure Time API

This project was forked from https://github.com/mathhomework/at_api. While the
initial effort was not maintained for long-term use, this fork is an attempt to
upgrade it to modern versions of Django, scrapy, celery, etc. and get it
running again in order to generate a demo project dataset.

The original project was unliscensed so I have reached out to the author,
Andrew, and will see about adding an open source liscense ASAP.

## Set up

This project is set up to run locally with Docker:

1. Install [Docker](https://docs.docker.com/install/)
   and [Docker Compose](https://docs.docker.com/compose/install/)
1. Copy the `.env` file: `cp template.env .env`
1. Build and run the application containers using docker-compose:
   ```
   $ docker-compose up --build -d
   ```
1. View the running application in a browser at http://localhost

### Set up without Docker

If you don't want to use Docker, you can run the app locally:

1. Create a virtual environment: `python3 -m venv .venv`
1. Activate the virtual environment: `. ./.venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Set environment variables:
   ```
   export SECRET_KEY=dev
   export DEBUG=True
   export ALLOWED_HOSTS=127.0.0.1,localhost
   ```
1. Migrate the database: `python manage.py migrate`
1. Collect static files: `python manage.py collectstatic --noinput`
1. Run the dev server: `python manage.py runserver`
1. View the running application in a browser at http://localhost:8000

## Helpful Links

- [Python](https://www.python.org/)
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Docker](https://docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [nginx](https://nginx.org/en/)
