from .configs.config_json import *
from .configs.app_list import *

import os

settings = get_settings()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = settings['SECRET_KEY']
DEBUG = settings['DEBUG']
ALLOWED_HOSTS = []

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'facturacionTennat.urls'

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

WSGI_APPLICATION = 'facturacionTennat.wsgi.application'
DATABASES = settings['DB']
AUTH_PASSWORD_VALIDATORS = settings['AUTH_PASSWORD_VALIDATORS']
LANGUAGE_CODE = settings['LANGUAGE_CODE']
TIME_ZONE = settings['TIME_ZONE']
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'q7i!bu_%jjxj-(kr=dxp7t9my9i9h&^&#llbz-o)+girovo(m1'
# SECURITY WARNING: don't run with debug turned on in production!

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


