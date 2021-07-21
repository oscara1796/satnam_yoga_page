"""
Django settings for satnam_yoga project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'satnamyoga.herokuapp.com', 'satnamyogaestudio.com', 'www.satnamyogaestudio.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Local apps:
    'ckeditor',
    'users.apps.UsersConfig',
    'videos.apps.VideosConfig',
    'posts',
    'payments.apps.PaymentsConfig',
    'contact',
    'pages.apps.PagesConfig',
    'BruteBuster',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'BruteBuster.middleware.RequestMiddleware',
    'satnam_yoga.middleware.profile_payment_completion_middleware',
    # 'satnam_yoga.middleware.user_profile_completion_middleware',
    'satnam_yoga.middleware.user_profile_paypal_account_verify_is_active_middleware'
]

ROOT_URLCONF = 'satnam_yoga.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'satnam_yoga.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'satnam',
        # 'NAME': 'dbsatnam',
        'USER': 'oscar',
        # 'USER': 'root',
        'PASSWORD': os.environ.get('DB_PASS_SATNAM'),
        'HOST':  os.environ.get('DB_HOST_SATNAM'),
        # 'PASSWORD': 'toor',
        # 'HOST':  'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT =  BASE_DIR / 'media'
STATIC_ROOT =  BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'

STATICFILES_DIRS =[os.path.join(BASE_DIR,"static")]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# STRIPE
STRIPE_PRICE_ID = "price_1I2MMzJQ5QjlwW1LnS05dQQj"
STRIPE_PRODUCT_ID = "prod_IddeskIwOYslF2"
STRIPE_PRICE_YEAR_ID = "price_1IlMcXJQ5QjlwW1Lk0t0Z3kY"
STRIPE_PRODUCT_YEAR_ID = "prod_JO8umebEYZdtA7"
STRIPE_PUBLISHABLE_KEY = 'pk_live_51Hy78jJQ5QjlwW1LttQugFTeDWJWFioiE6Oo2fquALWEb0aUM0kgmyxVmzQLn1avbsM0Puv5Ypb5XIyZtJnCJqW200RRuJfVfv'
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY_SATNAM')
STRIPE_ENDPOINT_SECRET  = os.environ.get('STRIPE_ENDPOINT_SECRET_SATNAM')

#ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat'],
            ['FontSize'],
            ['Font'],
            ['Format']
        ],
    }
}


#Email Config
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT= '587'
EMAIL_HOST_USER= 'satnamyogajal@hotmail.com'
EMAIL_HOST_PASSWORD= os.environ.get('EMAIL_HOST_PASSWORD_SATNAM')
EMAIL_USE_TLS= True
DEFAULT_FROM_EMAIL = 'satnamyogajal@hotmail.com'
SERVER_EMAIL = 'satnamyogajal@hotmail.com'
# EMAIL_USE_SSL= False

LOGIN_URL='login'

# PAYPAL INFO
# PAYPAL_CLIENT_ID = 'AY86OU5VjDXN_nDheNxF6xVMtK50JnQmA-1SxR8M1TJCj48tk0EYF9-yaqFYFEzhG-o8gjdPvNPYOWRU'
PAYPAL_CLIENT_ID = 'AUPzUZNqLg2hEQ4tJUb-tpQIxk7zZtLfi5LvsacyyP46L4VQgBkgy2C6uVJHVk5LLFNMR_TE5cUA7llg'
# PAYPAL_SECRET_ID = 'EK0__GZD3G68m18l90pankZhHFB7FNd3CKXSjL9Alz6OdISom4iFM85rM5FbC_UX019vtapOmIUfgh7g'
PAYPAL_SECRET_ID = os.environ.get('PAYPAL_SECRET_ID_SATNAM')
URL_PAYPAL_TOKEN = 'https://api.paypal.com/v1/oauth2/token'
PAYPAL_WEEBHOOK_ID =os.environ.get('PAYPAL_WEEBHOOK_ID_SATNAM')


BB_MAX_FAILURES= 5
BB_BLOCK_INTERVAL= 5

# django-storages
AWS_QUERYSTRING_AUTH= False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID_SATNAM')
AWS_SECRET_ACCESS_KEY= os.environ.get('AWS_SECRET_ACCESS_KEY_SATNAM')
AWS_STORAGE_BUCKET_NAME='satnam-bucket'


if os.getcwd() == '/app':
    SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT= True
    DEBUG= False

django_heroku.settings(locals())
