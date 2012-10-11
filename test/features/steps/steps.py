from behave import *
from selenium import webdriver 

@given('we have opened the browser for "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)

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


@then('we should see "{text}"')
def step(context,text):
    page_source = context.browser.page_source
    assert text in page_source

@then('we enter in the page with this title "{text}"')
def step(context, text):
    titlebrowser = context.browser.title 
    assert titlebrowser == text
 
@then('we logout')
def step(context):
    a = context.browser.find_element_by_link_text('Log out')
    a.click()

@then('we close de browser')
def step(context):
    context.browser.close()

