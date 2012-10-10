from behave import *
from selenium import webdriver 

@when('we enter in the courser list')
def step(context):
	a = context.browser.find_element_by_link_text('Courses')
	a.click()

@then('we should see "{text}"')
def step(context,text):
	form = context.browser.find_element_by_id('changelist-form')