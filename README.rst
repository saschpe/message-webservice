Message Webservice
==================

A Django website that provides pull notifications to subscribers (such as
Android or iOS apps). Apps can query messages based on their version.


Requirements
------------

- `Python 3`_


Hacking
-------

This project uses a virtual environment, activate it with this command:

.. code:: bash

    source .venv/bin/activate

To install all the project's development dependencies:

.. code:: bash

    pip install -r requirements/dev.txt

To set up the database and load initial data run:

.. code:: bash

    python manage.py migrate
    python manage.py loaddata notifications/fixtures/initial_data.json

To set up a (super) user for the admin interface:

.. code:: bash

    python manage.py createsuperuser

Afterwards, you should have a fully functional instance at

    http://127.0.0.1:8000/

Since there is no real browseable web interface, you'll be redirected to the
admin interface right away. The REST API is accessible at

    http://127.0.0.1:8000/api/v1?format=json

Makes use of two additional Django modules:

    https://django-modeltranslation.readthedocs.org
    https://django-tastypie.readthedocs.org


Deployment
----------

The simplest way to deploy this application is via docker_. Assuming you have
docker_ setup, you can simply do:

.. code:: bash

    ./bin/docker-build
    ./bin/docker-run



.. _Python 3: https://www.python.org/downloads/
.. _docker: https://www.docker.com/
