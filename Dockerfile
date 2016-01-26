FROM python:3
MAINTAINER Sascha Peilicke <sascha.peilicke@hotel.de>

RUN mkdir -p /usr/src/app/requirements
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
        freetds-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements/prod.txt
RUN python manage.py collectstatic --settings 'website.settings.prod' --no-input 

EXPOSE 81
CMD ["./bin/run"]
