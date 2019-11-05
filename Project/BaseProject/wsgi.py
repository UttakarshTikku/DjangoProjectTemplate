"""
WSGI config for BaseProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BaseProject.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Develop')

application = get_wsgi_application()
