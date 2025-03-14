import os
import subprocess

def create_additional_files(base_path):
    additional_files = {
        "Ma2tA/ma2ta/celery.py": celery_py_content,
        "Ma2tA/ma2ta/__init__.py": init_py_content,
        "Ma2tA/ma2ta/settings/__init__.py": init_py_content,
        "Ma2tA/ma2ta/settings/base.py": settings_base_py_content,
        "Ma2tA/ma2ta/settings/production.py": settings_production_py_content,
        "Ma2tA/ma2ta/settings/development.py": settings_development_py_content,
        "Ma2tA/ma2ta/settings/local.py": settings_local_py_content,
        "Ma2tA/Procfile": procfile_content,
    }
    for file_path, content in additional_files.items():
        os.makedirs(os.path.dirname(os.path.join(base_path, file_path)), exist_ok=True)
        with open(os.path.join(base_path, file_path), 'w') as file:
            file.write(content)

def initialize_git_repo(base_path):
    os.chdir(base_path)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "config", "--global", "user.name", "galleryma2ta"])
    subprocess.run(["git", "config", "--global", "user.email", "mohammadali.basirifar@gmail.com"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/galleryma2ta/Ma2tA.git"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

celery_py_content = """from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ma2ta.settings')

app = Celery('ma2ta')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
"""

init_py_content = ""

settings_base_py_content = """from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-#your-secret-key#'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'shop',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ma2ta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ma2ta.wsgi.application'

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

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
"""

settings_production_py_content = """from .base import *

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
"""

settings_development_py_content = """from .base import *

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
"""

settings_local_py_content = """from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

procfile_content = """web: gunicorn ma2ta.wsgi --log-file -
worker: celery -A ma2ta worker --loglevel=info
"""

# How to use
if __name__ == "__main__":
    project_base = os.getcwd()
    create_additional_files(project_base)
    initialize_git_repo(os.path.join(project_base, "Ma2tA"))