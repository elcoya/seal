from behave import *
from selenium import webdriver
from django.core.exceptions import ObjectDoesNotExist

import sys
sys.path.append("/home/martin/workspace/seal/seal")
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
    nCourses = Course.objects.count()
    assert nCourses == 0
            
@given('course "{course}" exists')
def step(context,course):
    try:
        c = Course.objects.get(name=course)
    except ObjectDoesNotExist:
        assert False 