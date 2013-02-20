import os, sys

project_base_path = os.path.realpath(os.path.dirname(__file__))
WEB_PATH = project_base_path + "/web/"
MODEL_PATH = project_base_path + "/web/seal/"
sys.path.append(WEB_PATH)           # Required to use the app model
sys.path.append(MODEL_PATH)         # Fixes 'No module named model'
os.environ['DJANGO_SETTINGS_MODULE'] = 'seal.settings'
os.environ['PROJECT_PATH'] = project_base_path + "/"
    

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()