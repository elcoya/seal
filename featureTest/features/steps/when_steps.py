from behave import *
from selenium import webdriver 

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
