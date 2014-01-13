# Django settings for seal project.
# -*- coding: utf-8 -*-

#FOR APACHE###
#DEBUG = False
##############
DEBUG = True 

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('seal', 'seal@foo.foo'),
)

MANAGERS = ADMINS

#Key for captcha
RECAPTCHA_PUB_KEY = "6LcuRdkSAAAAAOeCTPJ-FMf19ZOvVqRxdQjWgERE"
RECAPTCHA_PRIVATE_KEY = "6LcuRdkSAAAAAAnez1roxSgBbTfQ_iPxPhOnv5vP"

import os
web_base_path = os.path.realpath(os.path.dirname(__file__))

#path customizables############################################################
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
WORKSPACE_PATH = BASE_PATH + "/workspace/"
DELIVERY_FILE_PATH = WORKSPACE_PATH + "delivery_files/"
PRACTICE_FILE_PATH = WORKSPACE_PATH + "practice_files/"
SCRIPT_FILE_PATH = WORKSPACE_PATH + "automatic_correction_scripts/"
###############################################################################

#user and password for database create
USER="jarvis"
PASSWORD="jarvis"

DATABASES = {
    'default': {
        #FOR SQLITE##############################
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': web_base_path + '/seal.db',  
        #########################################
        
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jarvis',                     # Or path to database file if using sqlite3.
        'USER': USER,                      # Not used with sqlite3.
        'PASSWORD': PASSWORD,                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# To run the features test LANGUAGE_CODE = 'en-en'
LANGUAGE_CODE = 'en-en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#FOR APACHE########################################################
#MEDIA_ROOT = WORKSPACE_PATH
####################################################################
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#FOR APACHE################################
#MEDIA_URL = 'http://localhost:8000/media/'
###########################################
MEDIA_URL = '' 

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#FOR APACHE##################################
#STATIC_URL = 'http://localhost:8000/static/'
#############################################
STATIC_URL = '/static/' 

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('seal.auth.rest_api_permissions.ApplicationKeyPermission',),
    'PAGINATE_BY': 10
}

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    web_base_path + '/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# URL of the login page.
LOGIN_URL = '/login/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')q&!5_ig&s8h3w#l@2i#yn*=@6lhct+za(zpcb+%6p&@&^q-lv'

# Make this unique and don't share it. It must concur with the one setted for the daemon
DAEMON_KEY = 'seal-daemon-authentication-key'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Español'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # this middleware must be uncoment to change the lenguaje
    'django.middleware.locale.LocaleMiddleware',
)


ROOT_URLCONF = 'seal.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    web_base_path + '/templates/'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'rest_framework',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'bootstrap_toolkit',
    'model',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

