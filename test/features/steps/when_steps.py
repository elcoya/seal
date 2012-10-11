from behave import *
from selenium import webdriver 

@when('we log in as "{usr}" "{passwd}"')
def step(context, usr, passwd):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('username').send_keys(usr)
    form.find_element_by_name('password').send_keys(passwd)
    form.submit()

@when('we input login data "{loginData}"')
def step(context, loginData):
    form = context.browser.find_element_by_tag_name('form')
    splitted = loginData.split('|')
    form.find_element_by_name('username').send_keys(splitted[0])
    form.find_element_by_name('password').send_keys(splitted[1])
    form.submit()

@when('we enter in the course list')
def step(context):
    a = context.browser.find_element_by_link_text('Courses')
    a.click()

@when('course "{course}" exists')
def step(context,course):
    print(course)
    c = context.browser.find_element_by_link_text(course)