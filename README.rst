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

To install all the projects dependencies:

.. code:: bash

    pip install -r requirements.txt

To set up the database run:

.. code:: bash

    python manage.py migrate

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

Based on docker_, to be done...


.. _Python 3: https://www.python.org/downloads/
.. _docker: https://www.docker.com/
