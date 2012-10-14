from behave import *
from selenium import webdriver


import sys
sys.path.append("/home/anibal/workspace/python-aptana-wkspace/seal/")
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'seal.settings'

from seal.model.models import Course

@given('I have opened the browser for "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)

@given('I log in as "{usr}" "{passwd}"')
def step(context, usr, passwd):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('username').send_keys(usr)
    form.find_element_by_name('password').send_keys(passwd)
    form.submit()

@given('I am in the course list page')
def step(context):
    print(context)
    context.browser.get('http://localhost:8000/admin/model/course/')

@given('there are no courses')
def step(context):
    from seal.model.models import Course
    print('delete all courses...')
    
            
@given('course "{course}" exists')
def step(context,course):
    from seal.model.models import Course
    c = Course(name=course)
    #c.save()