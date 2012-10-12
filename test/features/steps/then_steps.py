from behave import *
from selenium import webdriver 

@then('I should see "{text}"')
def step(context,text):
    body = context.browser.find_element_by_tag_name('body')
    assert text in body.text

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

