"""
Django settings for peppertools project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
import datetime
import django_heroku
from django.utils.timezone import activate
from oscar.defaults import *


from django.utils.translation import gettext_lazy as _



OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('Correios'),
        'icon': 'icon-map-marker',
        'children': [
            {
                'label': _('Postagens'),
                'url_name': 'correios-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff
            },
        ]
    })

OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('Accounts'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Accounts'),
                'url_name': 'accounts_dashboard:accounts-list',
            },
            {
                'label': _('Transfers'),
                'url_name': 'accounts_dashboard:transfers-list',
            },
            {
                'label': _('Deferred income report'),
                'url_name': 'accounts_dashboard:report-deferred-income',
            },
            {
                'label': _('Profit/loss report'),
                'url_name': 'accounts_dashboard:report-profit-loss',
            },
        ]
    })


location = lambda x: os.path.join(
os.path.dirname(os.path.realpath(__file__)), x)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm51l@4%c42^q2c2o9l72o@&nc&@ssr93%yrwn5zj5phf2*)520'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True
THUMBNAIL_DEBUG = True
ALLOWED_HOSTS = ['peppertools.herokuapp.com', 'peppertools.lauromtp.com', 'localhost:8000']

MEDIA_URL = '/media/'
MEDIA_ROOT = location('media')

THUMBNAIL_KEY_PREFIX = 'oscar-sandbox'


# Application definition

INSTALLED_APPS = [
    'api',
    'rest_framework',
    'rest_framework_simplejwt',
    'easy_pdf',
    'pepperadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.gis',

    'oscar.config.Shop',
    'custom_apps.analytics.apps.AnalyticsConfig',
    'oscar.apps.checkout.apps.CheckoutConfig',
    'oscar.apps.address.apps.AddressConfig',
    'oscar.apps.shipping.apps.ShippingConfig',
    'custom_apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'custom_apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'custom_apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'custom_apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    'oscar_accounts.apps.AccountsConfig',
    'oscar_accounts.dashboard.apps.AccountsDashboardConfig',
    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',
    'paypal',
    'pysigep',
    'localflavor',
    'simple_history',
  
    'django_object_actions',
  
    'qrcode',
    'commerce',
    
   
    
  

] 

STRIPE_SECRET_KEY = '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'

STRIPE_PUBLISHABLE_KEY = 'pk_live_2lmD8loxvIHHUo2xwRRkRd6C00UtozvR6W'

STRIPE_CURRENCY = "BRL"

ADYEN_IDENTIFIER = 'Peppertools'

ADYEN_SKIN_CODE = '1xzvdIQD'

ADYEN_SECRET_KEY = '761C814D2F15FC6FDDAA506804924C0FA010D9BC0A4E3F8A8066A825BED16F4B'

ADYEN_ACTION_URL = 'https://test.adyen.com/hpp/cse/js/8216250740900522.shtml'

INSTALLED_APPS += ['paypal.express.dashboard.apps.ExpressDashboardApplication']

MERCADOPAGO = {
    'autoprocess': True,
    'success_url': 'django_mercadopago:mp_success',
    'failure_url': 'django_mercadopago:mp_failure',
    'pending_url': 'django_mercadopago:mp_pending',
    'base_host': 'localhost:8000'
}


SITE_ID = 1

PAYPAL_API_USERNAME = 'sb-fkkmx6656268_api1.business.example.com'
PAYPAL_API_PASSWORD = '2GUSZJEHNJNKPF6Y'
PAYPAL_API_SIGNATURE = 'AJNToUO45e9kLOTlLpVzI198s-T0AbKhPrCmAraNQAC48e.x3xSC0WSp'

OSCAR_DEFAULT_CURRENCY = 'BRL'
OSCAR_SHOP_NAME = 'Peppertools'
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}


AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
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
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
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
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
                
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
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dj6c9d4qm0jg', 
        'USER': 'qlwomodhbwxnas', 
        'PASSWORD': 'f84b47c547f9a0ff4c2b2f66c6d5fead66fa1ddc84727f053a1bf00908c90365',
        'HOST': 'ec2-54-157-100-65.compute-1.amazonaws.com', 
        'PORT': '5432',
    }
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
'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=3600),
'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=20),
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
PROJECT_ROOT   =   Path(__file__).resolve(strict=True).parent.parent
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
    os.path.join(BASE_DIR, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'






prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')


django_heroku.settings(locals())



#ALLOWED_HOSTS = ['peppertools.herokuapp.com']


activate(TIME_ZONE)
