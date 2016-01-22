from website.settings import *

DEBUG = True 
INSTALLED_APPS += (
    'debug_toolbar',  # and other apps for local development
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.sqlite3'),
    }
}
