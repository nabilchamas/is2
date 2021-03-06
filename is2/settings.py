"""
Django settings for is2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l8#*7b2=gx=l7%lkun%z2k0oj!0a(fbk*d+sa5@nx(5*x*6lmz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'apps.proyecto',
    'apps.usuario',
    'apps.inicio',
    'apps.perfil',
    'apps.flujo',
    'apps.userstory',
    'apps.sprint',
    'bootstrapform',
    'apps.burndownchart',
    'chartit',
    'simplejson',
    'db_file_storage',
    'archivos',
    'django_nose',
    'music',
)

DEFAULT_FILE_STORAGE = 'db_file_storage.storage.DatabaseFileStorage'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ROOT_URLCONF = 'is2.urls'

WSGI_APPLICATION = 'is2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# desarrollo
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }

# produccion
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'is2_produccion',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-PY'

TIME_ZONE = 'America/Asuncion'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATIC_URL = '/static/'

LOGIN_URL = '/inicio/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# DATE_INPUT_FORMATS = ('%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d',
#                       '%b %d %Y', '%b %d, %Y', '%d %b %Y',
#                       '%d %b, %Y', '%B %d %Y', '%B %d, %Y',
#                       '%d %B %Y', '%d %B, %Y')
# from django.conf.locale.en import formats
# formats.DATE_INPUT_FORMATS = DATE_INPUT_FORMATS


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'is2.r12.2015@gmail.com'
EMAIL_HOST_PASSWORD = 'carolinacarolina'
