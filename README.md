Hospital Management System

A Django-based Hospital Management System with PostgreSQL database. Includes models for doctors, patients, and appointments, and directly opens the admin panel.

Features

Manage doctors, patients, and appointments.

Directly open Django admin panel.

PostgreSQL backend.

REST API ready via Django REST Framework.

Requirements

Python 3.14+

Django 5.x+

PostgreSQL 16+

pip

Setup Instructions
1. Clone the repository
git clone <your-github-repo-url>
cd hospital_management_project

2. Install dependencies
pip install -r requirements.txt


If requirements.txt is not present:

pip install django psycopg2-binary djangorestframework python-dotenv

3. Configure database

Ensure PostgreSQL is running and your credentials in hospital_management/settings.py are correct:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hospital_db',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

4. Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

5. Run the development server
python3 manage.py runserver


Access the admin panel directly:

http://127.0.0.1:8000/admin
