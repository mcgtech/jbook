"""
Django settings for jbook project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '75n7jc7((g7^7b&^+82k^1y&9=6d67udq#f%f57sun9vfnr&y4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    'property',
    'booking',
    'crequest',
    'django_countries',
    'widget_tweaks',
    'django_tables2',
    'crispy_forms',
    'constance',
    'bootstrap_pagination',
]

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'GEN_FROM_EMAIL_ADDRESS': ('mcgonigalstephen@gmail.com', 'General from address'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'General Options': ('GEN_FROM_EMAIL_ADDRESS',),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jbook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates/registration',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]

WSGI_APPLICATION = 'jbook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jbook',
        'USER': 'jbook_admin',
        'PASSWORD': 'sa2342Dfsdxx*5$',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-GB'

TIME_ZONE = 'Europe/London'

USE_I18N = False

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# when on remote enable the following and run  ./manage.py collectstatic
# STATIC_ROOT = "/var/www/django_projs/static/"
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# STATIC_URL = '/static/'
# PROJECT_DIR = os.path.dirname(__file__)
# STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'),)

STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(__file__)
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'),)

LOGIN_URL = 'jbook_login'
LOGOUT_URL = 'jbook_logout'
LOGIN_REDIRECT_URL = 'login_success'

# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATE_INPUT_FORMATS = ('%d/%m/%Y')
#DATE_INPUT_FORMATS = ('%d/%m/%Y','%Y-%m-%d')

DISPLAY_DATE = '%d/%m/%Y'
DISPLAY_TIME = '%H:%M:%S'
DISPLAY_DATE_TIME = '%d/%m/%Y %H:%M:%S'
FILENAME_DATE_TIME = '%Y%m%d-%H%M%S'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# groups
ADMIN_GROUP = 'admin'
BO_GROUP = 'back office'

# https://github.com/jakubroztocil/django-settings-export
# allows us to access constants inside templates
SETTINGS_EXPORT = [
    'ADMIN_GROUP',
    'BO_GROUP',
]
# Message types
INFO_MSG_TYPE = 0
SUCC_MSG_TYPE = 1
WARN_MSG_TYPE = 2
ERR_MSG_TYPE = 3
DEBUG_MSG_TYPE = 4

BASE_URL = 'http://127.0.0.1:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
