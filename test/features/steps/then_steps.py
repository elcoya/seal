from behave import *
from selenium import webdriver 
from selenium.webdriver.common.by import By

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
    
@then('we should seee "{course1}" before "{course2}"')
def spep(context, course1, course2):
    trs = context.browser.find_elements(By.TAG_NAME, "tr")
    trs[1].find_element_by_link_text(course1)
    trs[2].find_element_by_link_text(course2)
