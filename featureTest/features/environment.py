from behave import *
from parse import *
from selenium import webdriver
from django.core.exceptions import ObjectDoesNotExist

# The next few steps are required to load the configuration and include the application model for the behavioural tests.
import ConfigParser, os
config = ConfigParser.ConfigParser()
config.readfp(open('../conf/local.cfg'))
import sys
sys.path.append(config.get("Path", "path.project"))		 # Required to use the app model
sys.path.append(config.get("Path", "path.behave.model")) # Fixes 'No module named model'
os.environ['DJANGO_SETTINGS_MODULE'] = 'seal.settings'

# Now we can load our model
from seal.model.course import Course


def create_super_user():
    # create a super user
    from django.contrib.auth.models import User
    u = User.objects.create(
        username='seal',
        first_name='Seal',
        last_name='Administrator',
        email='seal@gmail.com',
        is_superuser=True,
        is_staff=True,
        is_active=True
    )
    u.set_password('seal')
    u.save()
    print "User account created"
    
def before_all(context):
    create_super_user()

def before_feature(context, feature):
    if ('see the course list' in feature.name):
        context.browser = webdriver.Firefox()
        context.browser.get('http://localhost:8000/admin/')
        form = context.browser.find_element_by_tag_name('form')
        form.find_element_by_name('username').send_keys('seal')
        form.find_element_by_name('password').send_keys('seal')
        form.submit()
        print(context)
    
def after_feature(context, feature):
    if ('see the course list' in feature.name):
        a = context.browser.find_element_by_link_text('Log out')
        a.click()
        context.browser.close()

def before_scenario(context, scenario):
    if ('No courses' in scenario.name):
        print('delete all courses...')
        courses = Course.objects.all()
        courses.delete()

def before_step(context, step):
    if ('exists' in step.name):
        p = parse('course "{course}" exists', step.name)
        try:
            c = Course.objects.get(name=p['course'])
        except ObjectDoesNotExist:
            c = Course(name=p['course'])
            c.save()  
