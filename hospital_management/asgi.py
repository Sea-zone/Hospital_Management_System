# hospital_management/asgi.py
import os
from django.core.asgi import get_asgi_application

# Set the default settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_management.settings')

# Create ASGI application
application = get_asgi_application()
