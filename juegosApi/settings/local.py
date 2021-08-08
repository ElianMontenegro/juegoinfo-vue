from .base import *

#
import firebase_admin
from firebase_admin import credentials

DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'jusgosapidb',
        'USER': 'elian',
        'PASSWORD': 'OLAVARRIA18491',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]


cred = credentials.Certificate("fbkey.json")
firebase_admin.initialize_app(cred)