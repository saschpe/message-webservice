FROM ubuntu
LABEL maintainer="Sascha Peilicke <sascha@peilicke.de"
LABEL description="A Django website that provides pull notifications to subscribers (such as Android or iOS apps). Apps can query messages based on their version."

# Install prerequisites
RUN apt-get update && apt-get install -y \
        gcc git \
        python3-pip python3-dev python3-setuptools python3-wheel \
        freetds-dev libyaml-dev \
        nginx supervisor \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set up Django app
COPY . /opt/app
WORKDIR /opt/app
RUN pip3 install -r requirements/prod.txt
RUN python3 manage.py collectstatic --settings 'website.settings.prod' --no-input -v 0

# Set up nginx and supervisord
RUN rm /etc/nginx/sites-enabled/default
COPY contrib/nginx /etc/nginx
COPY contrib/supervisor /etc/supervisor
RUN mkdir -p /opt/app/log

EXPOSE 80
CMD ["./contrib/entrypoint"]
