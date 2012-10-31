from behave import *
from selenium import webdriver 

import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('../conf/local.cfg'))
pathproject = config.get("Path", "path.project")

@when('I log in as "{usr}" "{passwd}"')
def step(context, usr, passwd):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('username').send_keys(usr)
    form.find_element_by_name('password').send_keys(passwd)
    form.submit()

@when('I input login data "{loginData}"')
def step(context, loginData):
    form = context.browser.find_element_by_tag_name('form')
    splitted = loginData.split('|')
    form.find_element_by_name('username').send_keys(splitted[0])
    form.find_element_by_name('password').send_keys(splitted[1])
    form.submit()

@when('I enter in the course list')
def step(context):
    a = context.browser.find_element_by_link_text('Courses')
    a.click()

@when('I fill the newstudent form with default data')
def step(context):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('name').send_keys('Dummy Student')
    form.find_element_by_name('uid').send_keys('00000')
    form.find_element_by_name('email').send_keys('dummy@foo.foo')

@when('I submit the form')
def step(context):
    form = context.browser.find_element_by_tag_name('form')
    form.submit()
    
@when('I click in the "{text}" link')
def step(context, text):
    a = context.browser.find_element_by_link_text(text)
    a.click()
    
@when(u'I am at the new practice form')
def step(context):
    context.browser.get('http://localhost:8000/practices/newpractice')

@when(u'I fill the practice form with uid "{practice_uid}" and default data for course "{course_name}"')
def step(context, practice_uid, course_name):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('uid').send_keys(practice_uid)
    form.find_element_by_name('course').send_keys(course_name)
    filePath = pathproject + "featureTest/data/pdftest.pdf"
    print(filePath)
    form.find_element_by_name('file').send_keys(filePath)
    form.find_element_by_name('deadline').send_keys('2012-11-25')

@when('I change "{course1}" for "{course2}"')
def step(context, course1, course2):
    form = context.browser.find_element_by_tag_name('form')
    context.browser.find_element_by_id('id_name').clear()
    form.find_element_by_id('id_name').send_keys(course2)