from behave import *
from parse import *
from selenium import webdriver
from django.core.files import File

# The next few steps are required to load the configuration and include the application model for the behavioural tests.
import ConfigParser, os
config = ConfigParser.ConfigParser()
config.readfp(open('../conf/local.cfg'))
import sys
sys.path.append(config.get("Path", "path.project"))		 # Required to use the app model
sys.path.append(config.get("Path", "path.behave.model")) # Fixes 'No module named model'
os.environ['DJANGO_SETTINGS_MODULE'] = 'seal.settings'

pathproject = config.get("Path", "path.project")
filePath = pathproject + "featureTest/data/pdftest.pdf"

# Now we can load our model
from seal.model import Course, Student, Practice
from django.contrib.auth.models import User

def before_feature(context, feature):
        context.browser = webdriver.Firefox()
        context.browser.get('http://localhost:8000/')
        User.objects.exclude(username='seal').delete()
        Practice.objects.all().delete()
        Student.objects.all().delete() # Given Students are authenticated users, can't delete them without deleting the users
        User.objects.exclude(username='seal').delete()
        Course.objects.all().delete()
        #form = context.browser.find_element_by_tag_name('form')
        #form.find_element_by_name('username').send_keys('seal')
        #form.find_element_by_name('password').send_keys('seal')
        #form.submit()
        #print(context)
    
def after_feature(context, feature):
        #a = context.browser.find_element_by_link_text('Log out')
        #a.click()
        Delivery.objects.all().delete()
        Practice.objects.all().delete()
        Student.objects.all().delete() # Given Students are authenticated users, can't delete them without deleting the users
        User.objects.exclude(username='seal').delete()
        Course.objects.all().delete()
        context.browser.close()
