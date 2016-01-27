from website.settings import *

DEBUG = True 
INSTALLED_APPS += (
    'debug_toolbar',  # and other apps for local development
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.sqlite3'),
    },
    'mssql-dev': {
        'ENGINE': 'sqlserver_pymssql',
        'HOST': 'tsf-dbdev-01.office.hotel.de:1433',
        'NAME': 'message-service-dev-1',
        'USER': 'HOTELDEOFFICE\...',
        'PASSWORD': '...'
    }
}
