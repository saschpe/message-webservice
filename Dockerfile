FROM django:onbuild
MAINTAINER Sascha Peilicke <sascha.peilicke@hotel.de>

ONBUILD RUN python manage.py loaddata notifications/fixtures/initial_data.json
ONBUILD RUN echo "HDE2014\!" > python manage.py createsuperuser --username admin --email "team_mobile@hotel.de"
