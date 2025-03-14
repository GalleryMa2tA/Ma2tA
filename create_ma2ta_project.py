import os

def create_folder_structure(base_path):
    """ساختار فولدرهای پروژه را ایجاد می‌کند."""
    folders = [
        "Ma2tA",
        "Ma2tA/ma2ta",
        "Ma2tA/ma2ta/settings",
        "Ma2tA/shop",
        "Ma2tA/static",
        "Ma2tA/media",
        "ma2ta-frontend",
        "ma2ta-frontend/src",
        "ma2ta-frontend/src/components",
        "Ma2tAApp",
        "Ma2tAApp/screens"
    ]
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

def create_files(base_path):
    """فایل‌های پروژه را ایجاد می‌کند."""
    files = {
        "Ma2tA/manage.py": manage_py_content,
        "Ma2tA/ma2ta/__init__.py": "",
        "Ma2tA/ma2ta/settings/__init__.py": "",
        "Ma2tA/ma2ta/settings/base.py": settings_base_py_content,
        "Ma2tA/ma2ta/settings/production.py": settings_production_py_content,
        "Ma2tA/ma2ta/settings/development.py": settings_development_py_content,
        "Ma2tA/ma2ta/settings/local.py": settings_local_py_content,
        "Ma2tA/ma2ta/urls.py": urls_py_content,
        "Ma2tA/ma2ta/wsgi.py": wsgi_py_content,
        "Ma2tA/shop/models.py": models_py_content,
        "Ma2tA/shop/views.py": views_py_content,
        "Ma2tA/shop/urls.py": shop_urls_py_content,
        "ma2ta-frontend/src/index.js": index_js_content,
        "ma2ta-frontend/src/components/ProductList.js": product_list_js_content,
        "Ma2tAApp/App.js": app_js_content,
        "Ma2tAApp/screens/ProductsScreen.js": products_screen_js_content,
        "Ma2tA/Procfile": procfile_content,
        "Ma2tA/requirements.txt": requirements_txt_content,
    }
    for file_path, content in files.items():
        with open(os.path.join(base_path, file_path), 'w') as file:
            file.write(content)

# محتوای فایل‌ها
manage_py_content = '''"""
Django's command-line utility for administrative tasks.
"""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ma2ta.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
'''

settings_base_py_content = '''from pathlib import Path

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
'''

settings_production_py_content = '''from .base import *

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
'''

settings_development_py_content = '''from .base import *

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
'''

settings_local_py_content = '''from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

urls_py_content = '''from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls', namespace='shop')),
]
'''

wsgi_py_content = '''"""
WSGI config for ma2ta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ma2ta.settings')

application = get_wsgi_application()
'''

models_py_content = '''from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
'''

views_py_content = '''from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})
'''

shop_urls_py_content = '''from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
'''

index_js_content = '''import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import rootReducer from './reducers';
import App from './App';

const store = createStore(rootReducer);

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
);
'''

product_list_js_content = '''import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('/api/products/')
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the products!', error);
            });
    }, []);

    return (
        <div>
            <h1>Product List</h1>
            <ul>
                {products.map(product => (
                    <li key={product.id}>{product.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default ProductList;
'''

app_js_content = '''import React from 'react';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import rootReducer from './reducers';
import ProductsScreen from './screens/ProductsScreen';

const store = createStore(rootReducer);

const App = () => {
    return (
        <Provider store={store}>
            <ProductsScreen />
        </Provider>
    );
};

export default App;
'''

products_screen_js_content = '''import React, { useEffect, useState } from 'react';
import { View, Text, FlatList } from 'react-native';
import axios from 'axios';

const ProductsScreen = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://your-api-url/api/products/')
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the products!', error);
            });
    }, []);

    return (
        <View>
            <Text>Product List</Text>
            <FlatList
                data={products}
                keyExtractor={item => item.id.toString()}
                renderItem={({ item }) => (
                    <View>
                        <Text>{item.name}</Text>
                    </View>
                )}
            />
        </View>
    );
};

export default ProductsScreen;
'''

procfile_content = '''web: gunicorn ma2ta.wsgi --log-file -
worker: celery -A ma2ta worker --loglevel=info
'''

requirements_txt_content = '''Django
djangorestframework
psycopg2-binary
celery
redis
django-celery-results
gunicorn
'''

if __name__ == '__main__':
    base_path = os.getcwd()  # مسیر فعلی به عنوان مسیر پایه
    create_folder_structure(base_path)
    create_files(base_path)
    print("ساختار پروژه Ma2tA با موفقیت ایجاد شد.")