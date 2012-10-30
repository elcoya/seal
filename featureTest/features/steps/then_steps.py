from behave import *
from selenium import webdriver 
from selenium.webdriver.common.by import By

@then('I should see "{course1}" before "{course2}"')
def step(context, course1, course2):
    trs = context.browser.find_elements(By.TAG_NAME, "tr")
    course1 in trs[1].text
    course2 in trs[2].text

@then('I should see "{text}"')
def step(context,text):
    body = context.browser.find_element_by_tag_name('body')
    assert text in body.text

@then('I enter in the page with this title "{text}"')
def step(context, text):
    titlebrowser = context.browser.title 
    assert titlebrowser == text
 
@then('I logout')
def step(context):
    a = context.browser.find_element_by_link_text('Log out')
    a.click()

@then('I close de browser')
def step(context):
    context.browser.close()
