from behave import *
from selenium import webdriver 

@given('we have opened the browser for "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)

@when('we input login data "{loginData}"')
def step(context, loginData):
    form = context.browser.find_element_by_tag_name('form')
    splitted = loginData.split('|')
    form.find_element_by_name('username').send_keys(splitted[0])
    form.find_element_by_name('password').send_keys(splitted[1])
    form.submit()

@then('we enter in the page with this title "{text}"')
def step(context, text):
    titlebrowser = context.browser.title 
    assert titlebrowser == text
 
@then('we logout and close de browser')
def step(context):
    a = context.browser.find_element_by_link_text('Log out')
    a.click()
    context.browser.close()