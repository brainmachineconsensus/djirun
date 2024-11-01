import os
from datetime import date
from django.core.management import call_command
import sys
from rich.console import Console
import datetime




console = Console()

class Djirun:

    """
    A class to create and configure a Django project with various options.

    Attributes:
        project_name (str): The name of the Django project.
        app_name (str): The name of the Django application.
        css_framework (str): CSS framework to use (bootstrap, tailwind, none).
        create_static_structure (bool): Whether to create a static files structure.
        single_page (bool): Whether to create a single-page application.
        database (str): Database to use (sqlite, postgres).
        auth (bool): Whether to enable authentication.
        api (bool): Whether to enable REST API.
        i18n (bool): Whether to enable internationalization.
        tests (bool): Whether to add unit tests.
        docs (bool): Whether to generate documentation.
        docker (bool): Whether to add Docker configuration.
        python_version (str): Python version to use for Docker.
    """


    def __init__(self, project_name, css_framework='none', static_structure=False, single_page=False, database='sqlite', auth=False, api=False, i18n=False, tests=False, docs=False, docker=False, python_version=None):
        self.project_name = project_name
        self.app_name = 'core'
        self.css_framework = css_framework
        self.create_static_structure = static_structure
        self.single_page = single_page
        self.database = database
        self.auth = auth
        self.api = api
        self.i18n = i18n
        self.tests = tests
        self.docs = docs
        self.docker = docker
        self.python_version = python_version

    def check_python_version(self):

        """
        Checks and sets the Python version for Docker if not provided.
        """

        if self.python_version is None:
            # Obtenir la version actuelle de Python
            self.python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        # print(f"Using Python version: {self.python_version}")

    def handle(self):
    
        """
        Main method to handle the project creation and configuration process.

        Creates the Django project, modifies settings and URLs, and sets up additional configurations based on user inputs.
        """

        self.check_python_version()
        self.create_django_project()
        self.modify_settings()
        self.modify_urls()
        self.create_folder_structure()
        self.create_app_files()

        if self.auth:
            self.setup_authentication()
        if self.api:
            self.setup_rest_api()
        if self.i18n:
            self.setup_internationalization()
        if self.tests:
            self.setup_unit_tests()
        if self.docs:
            self.generate_documentation()
        if self.docker:
            self.generate_docker_config()


        self.setup_database()
        import time
        time.strftime("%Y")
        # print(f'Your Django project {self.project_name} has been successfully created by {self.app_name}')
        console.print(f'\nYeeeah!! Your Django project has been successfully generated by Djirun \n', style="green")
        console.print(f'Project name     : "{self.project_name}"\nDefault app name : "{self.app_name}"')
        console.print(f'Current pathwork : "{os.getcwd()}"',)
        console.print(f'Go to current pathwork and run "python manage.py runserver" to launch project', style="red")
        print(f'{date.today()} - {time.strftime("%H:%M:%S")}')
        console.print('Powered by Djirun...\n')

    def create_django_project(self):

        """
        Creates a new Django project and an application within it.

        The method uses Django management commands to generate the initial project and application structure.
        """

        call_command('startproject', self.project_name)
        os.chdir(self.project_name)
        call_command('startapp', self.app_name)

    def modify_settings(self):

        """
        Modifies the Django settings.py file to include static files, media files, and template configurations.

        Adds necessary configurations for static and media files, and updates the TEMPLATES setting to include the project templates directory.
        """

        settings_path = f'{self.project_name}/settings.py'
        
        
        with open(settings_path, 'r+') as f:
            content = f.read()
            content = content.replace(
                'from pathlib import Path',
                "import os\nfrom pathlib import Path"
            )

            content = content.replace(
                "'django.contrib.staticfiles',",
                f"'django.contrib.staticfiles',\n    '{self.app_name}',")
            
            content = content.replace(
                "'DIRS': []",
                "'DIRS': [BASE_DIR/'templates']"
            )
            
            content += '\n\n# Static files configuration\n'
            content += 'STATIC_URL = "/static/"\n'
            content += 'STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")\n'
            content += "STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)\n\n"
            content += '# Media files configuration\n'
            content += 'MEDIA_URL = "/media/"\n'
            
            content += '\n# Templates configuration\n'
            content += 'TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "templates")]\n'
            
            f.seek(0)
            f.write(content)
            f.truncate()

    def modify_urls(self):

        """
        Modifies the Django urls.py file to include the application's URLs and static/media file configurations.

        Updates the urlpatterns to include the app's URLs and configure the serving of static and media files.
        """

        urls_path = f'{self.project_name}/urls.py'
        with open(urls_path, 'r+') as f:
            content = f.read()
            content = content.replace(
                'from django.urls import path',
                'from django.urls import path, include\nfrom django.conf import settings\nfrom django.conf.urls.static import static')
            
            if self.single_page:
                content = content.replace(
                    'urlpatterns = [',
                    f'urlpatterns = [\npath("", include("{self.app_name}.urls")),')
            else:
                content = content.replace(
                    'urlpatterns = [',
                    f'urlpatterns = [\npath("", include("{self.app_name}.urls")),')
            
            content = content.replace(
                ']',
                f"]\nif settings.DEBUG:\n  urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)")
            f.seek(0)
            f.write(content)
            f.truncate()

    def create_folder_structure(self):

        """
        Creates the initial folder structure for templates, static files, and media files.

        Sets up directories for templates, static files, and media files based on the project's configuration.
        """
        base_template = {
            'bootstrap': '''{% load static %}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <title>Set the project name</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        {% block content %}
        {% endblock %}
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
</html>
''',

'tailwind': '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <title>Set the project name</title> 
    <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
</html>
''',
'none': '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <title>Set the project name</title>
</head>
    <body>
    {% block content %}
    {% endblock %}
    </body>
</html>
        
'''}


        os.makedirs('templates/base', exist_ok=True)
        with open('templates/base/base.html', 'w') as f:
            f.write(base_template[self.css_framework])  

        base_style = '''/*     CSS file generated by djirun    */

*, ::before, ::after{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
'''

        base_js_script = '''// Js file generated by djirun '''

        os.makedirs('static/css', exist_ok=True) # Basic CSS configuration
        with open('static/css/style.css', 'w') as f:
            f.write(base_style)

        os.makedirs('static/js', exist_ok=True) # Basic JS file configuration
        with open('static/js/script.js', 'w') as f:
            f.write(base_js_script)

        os.makedirs('static/images', exist_ok=True) # Image Folder configuration
        
        self.create_base_template()
        os.makedirs('media', exist_ok=True)

    def create_base_template(self):

        """
        Creates the base HTML template for the project based on the selected CSS framework.

        Writes a base template file that includes the necessary CSS framework links and basic HTML structure.
        """

        base_home = '''{% extends 'base/base.html' %}
{% load static %}
{% block content %}
<h1 style="height: 100vh; width: 100%; display: flex; justify-content: center; align-items: center;">
    Hello Djirun, This is Home Page. Enjoy !!
</h1>
{% endblock %}
      
'''

        with open('templates/index.html', 'w') as f:
            f.write(base_home)

    def create_app_files(self):

        """
        Creates initial files for the application, including views, URLs, and templates.

        Generates basic view and URL files, as well as a sample HTML template for the application.
        """

        # views.py
        with open(f'{self.app_name}/views.py', 'w') as f:
            f.write('''
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
            ''')
        
        # urls.py
        with open(f'{self.app_name}/urls.py', 'w') as f:
            f.write('''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
        ]
            ''')
        

    def setup_authentication(self):

        """
        Configures authentication URLs and settings in the Django project.

        Adds authentication URLs to the project's URL configuration.
        """

        settings_path = f'{self.project_name}/settings.py'
        with open(settings_path, 'r+') as f:
            content = f.read()
            if 'django.contrib.auth' not in content:
                content = content.replace(
                    'INSTALLED_APPS = [',
                    "INSTALLED_APPS = [\n    'django.contrib.auth',\n    'django.contrib.contenttypes',")
            f.seek(0)
            f.write(content)
            f.truncate()

    def setup_rest_api(self):

        """
        Sets up Django REST framework for API functionality.

        Installs Django REST framework and updates settings to include it.
        """

        os.system('pip install djangorestframework')

        # Ajouter 'rest_framework' dans INSTALLED_APPS
        settings_path = f'{self.project_name}/settings.py'
        with open(settings_path, 'r+') as f:
            content = f.read()
            if 'rest_framework' not in content:
                content = content.replace(
                    'INSTALLED_APPS = [',
                    "INSTALLED_APPS = [\n    'rest_framework',")
            f.seek(0)
            f.write(content)
            f.truncate()

    def setup_internationalization(self):

        """
        Enables internationalization settings in Django.

        Updates the settings to enable internationalization and localization features.
        """
        
        settings_path = f'{self.project_name}/settings.py'
        with open(settings_path, 'r+') as f:
            content = f.read()
            content += '''
            USE_I18N = True
            USE_L10N = True
            USE_TZ = True
            LANGUAGE_CODE = 'fr-fr'
            TIME_ZONE = 'Europe/Paris'
            '''
            f.seek(0)
            f.write(content)
            f.truncate()

    def setup_unit_tests(self):
        
        """
        Creates a basic unit test for the application.

        Writes a test case to check the status code of the home page.
        """

        os.makedirs(f'{self.app_name}/tests', exist_ok=True)
        with open(f'{self.app_name}/tests/test_views.py', 'w') as f:
            f.write('''
from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
            ''')

    def generate_documentation(self):

        """
        Generates a basic README file for the project.

        Creates a README.md file with a brief description of the project.
        """


        # Install Sphinx
        os.system('pip install sphinx sphinx-rtd-theme')

        # Crate config file and directory
        os.makedirs('docs', exist_ok=True)
        os.system('sphinx-quickstart docs')

    def generate_docker_config(self):
    
        """
        Creates Docker configuration files for the project.

        Generates Dockerfile and docker-compose.yml for containerization of the Django application.
        """
        
        # Checking python version
        python_version = self.python_version or f"{sys.version_info.major}.{sys.version_info.minor}"
        
        # Créer Dockerfile avec la version de Python spécifiée
        dockerfile_content = f'''
FROM python:{python_version}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", f"{self.project_name}.wsgi:application"]
'''

        with open('Dockerfile', 'w') as f:
            f.write(dockerfile_content)
        
        # Create docker-compose.yml
        docker_compose_content = f'''

# This is an docker-compose.yml exemple  template, customise

version: '{python_version}'

services:
web:
    build: .
    command: gunicorn {self.project_name}.wsgi:application --bind 0.0.0.0:8000
    volumes:
    - .:/app
    ports:
    - "8000:8000"
    depends_on:
    - db

db:
    image: postgres:13
    volumes:
    - postgres_data:/var/lib/postgresql/data
    environment:
    POSTGRES_DB: {self.project_name}_db
    POSTGRES_USER: user
    POSTGRES_PASSWORD: password

volumes:
postgres_data:
'''

        with open('docker-compose.yml', 'w') as f:
            f.write(docker_compose_content)

    def setup_database(self):

        """
        Sets up the initial database and creates a superuser.

        Applies migrations to set up the database schema and creates a default superuser.
        """

        if self.database == 'postgres':
            # Installer psycopg2 pour PostgreSQL
            os.system('pip install psycopg2-binary')

            # Ajouter la configuration PostgreSQL dans settings.py
            settings_path = f'{self.project_name}/settings.py'
            with open(settings_path, 'r+') as f:
                content = f.read()
                content = content.replace(
                    'DATABASES = {',
                    f"DATABASES = {{\n    'default': {{\n        'ENGINE': 'django.db.backends.postgresql',\n        'NAME': '{self.project_name}_db',\n        'USER': 'user',\n        'PASSWORD': 'password',\n        'HOST': 'db',\n        'PORT': '5432',\n    }}\n}}\n")
                f.seek(0)
                f.write(content)
                f.truncate()