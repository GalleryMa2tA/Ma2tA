from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ma2tadb',
        'USER': 'ma2tauser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
