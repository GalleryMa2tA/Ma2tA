from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your_domain.com']

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
