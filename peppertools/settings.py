"""
Django settings for peppertools project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime, django_heroku, dj_database_url, environ, os, sys, socket
from django.http import HttpRequest
from pathlib import Path
from django.utils.timezone import activate
#from oscar.defaults import *
from django.utils.translation import gettext_lazy as _

env = environ.Env()
environ.Env.read_env()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_URL = env('AWS_URL')
AWS_S3_REGION_NAME = 'sa-east-1'

HOMOG_USUARIO = env('HOMOG_USUARIO')
HOMOG_SENHA = env('HOMOG_SENHA')
HOMOG_CARTAO = env('HOMOG_CARTAO')
HOMOG_CODIGO_ADMIN = env('HOMOG_CODIGO_ADMIN')
HOMOG_CONTRATO = env('HOMOG_CONTRATO')
HOMOG_CNPJ = env('HOMOG_CNPJ')

STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_CURRENCY = env("STRIPE_CURRENCY")
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")
   
location = lambda x: os.path.join(
os.path.dirname(os.path.realpath(__file__)), x)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
#DEBUG_PROPAGATE_EXCEPTIONS = env('DEBUG')
THUMBNAIL_DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['pentercorp.herokuapp.com', 'peppertools.herokuapp.com', 'peppertools.lauromtp.com', 'localhost:8000', 'localhost:19006']

MEDIA_URL = '/media/'
MEDIA_ROOT = location('media')

THUMBNAIL_KEY_PREFIX = 'sandbox'


# Application definition

INSTALLED_APPS = [
    'api',
    'rest_framework',
    'rest_framework_simplejwt',
    'easy_pdf',
    'corsheaders',
    'pepperadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    # 'django.contrib.gis',
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',
    'pysigep',
    'localflavor',
    'simple_history',
  
    'django_object_actions',
  
    'qrcode',
   
    
   
    
  

] 

STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")

STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")

STRIPE_CURRENCY = env("STRIPE_CURRENCY")

ADYEN_IDENTIFIER = env('ADYEN_IDENTIFIER')

ADYEN_SKIN_CODE = env('ADYEN_SKIN_CODE')

ADYEN_SECRET_KEY = env('ADYEN_SECRET_KEY')

ADYEN_ACTION_URL = env('ADYEN_ACTION_URL')

# INSTALLED_APPS += ['paypal.express.dashboard.apps.ExpressDashboardApplication']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:19000',
    'http://localhost:19002',
    'http://localhost:19001',
    'http://localhost:3000',
    'http://localhost:19006'
]


MERCADOPAGO = {
    'autoprocess': True,
    'success_url': 'django_mercadopago:mp_success',
    'failure_url': 'django_mercadopago:mp_failure',
    'pending_url': 'django_mercadopago:mp_pending',
    'base_host': 'localhost:8000'
}


SITE_ID = 1

PAYPAL_API_USERNAME = env('PAYPAL_API_USERNAME')
PAYPAL_API_PASSWORD = env('PAYPAL_API_PASSWORD')
PAYPAL_API_SIGNATURE = env('PAYPAL_API_SIGNATURE')

# OSCAR_DEFAULT_CURRENCY = env('OSCAR_DEFAULT_CURRENCY')
# OSCAR_SHOP_NAME = env('OSCAR_SHOP_NAME')
# OSCAR_INITIAL_ORDER_STATUS = 'Pending'
# OSCAR_INITIAL_LINE_STATUS = 'Pending'
# OSCAR_ORDER_STATUS_PIPELINE = {
#     'Pending': ('Being processed', 'Cancelled',),
#     'Being processed': ('Processed', 'Cancelled',),
#     'Cancelled': (),
# }


AUTHENTICATION_BACKENDS = (
    # 'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    # 'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

MERCADOPAGO_AUTOPROCESS = False

ROOT_URLCONF = 'peppertools.urls'


SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'oscar.apps.search.context_processors.search_form',
                # 'oscar.apps.checkout.context_processors.checkout',
                # 'oscar.apps.communication.notifications.context_processors.notifications',
                # 'oscar.core.context_processors.metadata',
                
            ],


        'loaders': [
            ('django.template.loaders.cached.Loader', [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                
            ]),
        ],

        },
    },
]


WSGI_APPLICATION = 'peppertools.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dbtest'
    }




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [
      'rest_framework_simplejwt.authentication.JWTAuthentication',
     
    ],
      'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        
    ],
    
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

LOCALE_NAME = 'pt_BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=30),
'ROTATE_REFRESH_TOKENS': False,
'BLACKLIST_AFTER_ROTATION': True,

'ALGORITHM': 'HS256',
'SIGNING_KEY': SECRET_KEY,
'VERIFYING_KEY': None,
'AUDIENCE': None,
'ISSUER': None,

'AUTH_HEADER_TYPES': ('Bearer',),
'USER_ID_FIELD': 'id',
'USER_ID_CLAIM': 'user_id',

'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
'TOKEN_TYPE_CLAIM': 'token_type',

'JTI_CLAIM': 'jti',
'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=3600),
'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=20),
}



LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
PROJECT_ROOT   =  AWS_URL 
#Path(__file__).resolve(strict=True).parent.parent
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
GEOIP_PATH = os.path.join(PROJECT_ROOT,  'geoIP')



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_collect'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'






# prod_db  =  dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)
#DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')

STATIC_ROOT = AWS_URL + '/static/'
STATIC_URL = AWS_URL + '/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = AWS_URL + '/media/'
MEDIA_ROOT = AWS_URL + '/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
django_heroku.settings(locals(), staticfiles=False)





#ALLOWED_HOSTS = ['peppertools.herokuapp.com']


activate(TIME_ZONE)
