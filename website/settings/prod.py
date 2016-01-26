from website.settings import *

ALLOWED_HOSTS = '0.0.0.0'

DATABASES = {
    'default': {
        'ENGINE': 'sqlserver_pymssql',
        'HOST': 'tsf-db-01.prod.hotel.de:1433',
        'NAME': 'message-service',
        'USER': 'messaging-service',
        'PASSWORD': 'm1*Ess=7Ag!e'
    }
}

# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Clickjacking prevention
X_FRAME_OPTIONS = 'DENY'
