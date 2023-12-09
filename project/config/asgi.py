"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

dotenv_path = os.path.join('.env')
load_dotenv(dotenv_path)


if os.getenv('STATUS') == 'develope':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.develope')
if os.getenv('STATUS') == 'deployment':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.deployment')
if os.getenv('STATUS') == 'kubernetes':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.kubernetes')

application = get_asgi_application()
