FROM python:3.4
MAINTAINER Sascha Peilicke <sascha.peilicke@hotel.de>

RUN mkdir -p /usr/src/app/requirements
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements/prod.txt ;\
    export DJANGO_SETTINGS_MODULE="website.settings.prod" ;\
    python manage.py migrate ;\
    python manage.py loaddata notifications/fixtures/initial_data.json ;\
    echo "HDE2014\!" > python manage.py createsuperuser --username admin --email "team_mobile@hotel.de" ;\
    python manage.py collectstatic --settings 'website.settings.prod' --no-input 

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "--settings", "'website.settings.prod'", "0.0.0.0:8000"]
