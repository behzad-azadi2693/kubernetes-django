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

DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': 'localhost',
            'PORT': os.getenv('DB_PORT'),
        }
    }


# redis chache
CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": f"redis://localhost:{os.getenv('REDIS_PORT')}/1",
            'OPTIONS': {
                'PASSWORD': os.getenv('REDIS_PASSWORD'),
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }


REDIS_HOST = 'localhost'
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)


#This Config For djdt

INTERNAL_IPS = [
    "127.0.0.1",
]