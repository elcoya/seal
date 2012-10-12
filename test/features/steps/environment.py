from behave import *
from selenium import webdriver 

def before_scenario(context, scenario):
    if ('No courses' in scenario.name):
        context.browser = webdriver.Firefox()
        context.browser.get('http://localhost:8000/admin/')
        form = context.browser.find_element_by_tag_name('form')
        form.find_element_by_name('username').send_keys('seal')
        form.find_element_by_name('password').send_keys('seal')
        form.submit()
        print(context)

def after_scenario(context, scenario):
    if ('No courses' in scenario.name):
        a = context.browser.find_element_by_link_text('Log out')
        a.click()
        context.browser.close()
