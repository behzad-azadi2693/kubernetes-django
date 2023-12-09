from . import base
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.

dotenv_path = os.path.join(base.BASE_DIR, '.env')
load_dotenv(dotenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.getenv('WEB_DOMAIN'), f'www{os.getenv("WEB_DOMAIN")}', 'web']


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT'),
        }
    }



# redis chache
CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": f"redis://{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}/1",
            'OPTIONS': {
                'PASSWORD': os.getenv('REDIS_PASSWORD'),
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }


REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)