from behave import *
from selenium import webdriver 

import sys
sys.path.append("/home/martin/workspace/seal/")
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'seal.settings'

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
