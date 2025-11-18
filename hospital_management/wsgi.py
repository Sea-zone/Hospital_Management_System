# hospital_management/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_management.settings')

# Create WSGI application
application = get_wsgi_application()
