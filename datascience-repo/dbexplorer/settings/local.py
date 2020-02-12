"""Development settings and globals."""

from __future__ import absolute_import

from .common import * # noqa

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "dbexplorer",
        'USER': "",
        'PASSWORD': "",
        'HOST': "",
    },
    # 'employees': {
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': 'employees',
    #     'USER': 'SA',
    #     'PASSWORD': 'soul@123',
    #     'HOST': '127.0.0.1',
    #     'PORT': '1433'
    # },
    # 'developers': {
    #     'ENGINE': 'django.db.backends.mysql', 
    #     'NAME': 'developers',
    #     'USER': 'root',
    #     'PASSWORD': 'soul@123',
    #     'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
    #     'PORT': '3306',
    # },
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = ('127.0.0.1',)

CORS_ORIGIN_ALLOW_ALL = True