"""
Django settings for appMainSite project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-132+-6o**fxw)7h!)o#0i(wvs%cm_9tivdj3+=q$&rdyg@8yn5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.71', '18.223.162.255', '192.168.5.2', '127.0.0.1', 'yonk-e', '18.223.167.9', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
        'widget_tweaks',
    'tempus_dominus',
    'OBTaller',
    'OBTaller.operador',

    'OBTaller.loginus',
    'OBTaller.user',


]

# MIDDLEWARE_CLASSES = [
#     # 'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
#     'OBTaller.redirect.CustomRedirectFallbackMiddleware',
# ]

MIDDLEWARE = [
    'OBTaller.middleware.StatusMenu',
    'OBTaller.middleware.MenuReportes',
    # 'OBTaller.middleware.CustomRedirectFallbackMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'OBTaller.redirect.CustomRedirectFallbackMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'current_user.CurrentUserMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'appMainSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'appMainSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'sismbordb',
    'USER': 'admin',
    'PASSWORD': '123456',
    # 'PASSWORD': 'CveDb.123456',
    'HOST': 'localhost',
	# 'HOST': 'database-hotelweb.cjg26m5mzcaw.us-east-2.rds.amazonaws.com',

    'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_AUTOREFRESH = DEBUG
# WHITENOISE_USE_FINDERS = True

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))



STATIC_URL = '/static/'



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

URL_OPERADOR = 'registro'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

STATIC_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'static'))

AUTH_USER_MODEL = 'user.User'

BASE_URL_MEDIA = 'static/images/upload'
MEDIA_URL   = '/upload/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, BASE_URL_MEDIA)
# STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))
