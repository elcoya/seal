from behave import *
from parse import *
from selenium import webdriver
from django.core.files import File

# The next few steps are required to load the configuration and include the application model for the behavioural tests.
import ConfigParser, os
from django.contrib.auth import login
config = ConfigParser.ConfigParser()
config.readfp(open('../conf/local.cfg'))
import sys
sys.path.append(config.get("Path", "path.project"))		 # Required to use the app model
sys.path.append(config.get("Path", "path.behave.model")) # Fixes 'No module named model'
os.environ['DJANGO_SETTINGS_MODULE'] = 'seal.settings'

pathproject = config.get("Path", "path.project")
filePath = pathproject + "featureTest/data/pdftest.pdf"

# Now we can load our model
from seal.model import Course, Student, Practice, Delivery, Teacher
from django.contrib.auth.models import User

def before_all(context):
    User.objects.exclude(username='seal').delete()
    Practice.objects.all().delete()
    Course.objects.all().delete()
    Student.objects.all().delete() # Given Students are authenticated users, can't delete them without deleting the users
    Teacher.objects.all().delete()
    User.objects.exclude(username='seal').delete()
    uid = 'teacher'
    user = User()
    user.username = uid
    user.set_password(uid)
    user.email = uid + "@foo.foo"
    user.save()
    teacher = Teacher()
    teacher.user = user
    teacher.name = uid
    teacher.uid = uid
    teacher.email = uid + "@foo.foo"
    teacher.save()

def after_all(context):
    Delivery.objects.all().delete()
    Practice.objects.all().delete()
    Course.objects.all().delete()
    Student.objects.all().delete() # Given Students are authenticated users, can't delete them without deleting the users
    Teacher.objects.all().delete()
    User.objects.exclude(username='seal').delete()

def before_feature(context, feature):
    context.browser = webdriver.Firefox()
    context.browser.get('http://localhost:8000/')

def after_feature(context, feature):
    #a = context.browser.find_element_by_link_text('Log out')
    #a.click()
    context.browser.close()

def before_scenario(context, scenario):
    context.browser.get('http://localhost:8000/')
