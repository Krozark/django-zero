 # -*- coding: utf-8 -*-
"""
Django settings for zero project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEV= DEBUG
TEMPLATE_DEBUG = DEBUG
#DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

ALLOWED_HOSTS = []

SITE_ID = 1

ADMINS = (
        ('maxime BARBIER', 'maxime.barbier1991@gmail.com'),
)

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.db'),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i_zxx4*b(^v@-n$880it-gm$hi90x$o!q60^x^tf=)t6gbmap_'

LANGUAGE_CODE = 'en'
gettext = lambda s:s
LANGUAGES = (
        ('en',gettext(u'English')),
        ('fr',gettext(u'Français')),
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'public/media/')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'public/static/')
STATIC_URL = '/static/'
#ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
#STATICFILES_DIRS = (
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
#)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.media',
#    "django.core.context_processors.static", 
#    'django.core.context_processors.request',
#)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #'django.contrib.comments',
    #'django.contrib.messages',
    #'django.contrib.markup',

    'django.contrib.humanize',

    'rosetta',

    'debug_toolbar',
    #'raven.contrib.django.raven_compat',
    'django_extensions',
    'registration',

    #'taggit',

    'website',
)
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value

#RAVEN_CONFIG = {
    #your api key
    #create account https://www.getsentry.com/register/
    #'dsn': 'https://530251f72c084179872589d80ba05e71:630e4c96dd694cb48a4385f66dc2be06@app.getsentry.com/27531',
#}

ROOT_URLCONF = 'zero.urls'

WSGI_APPLICATION = 'zero.wsgi.application'

