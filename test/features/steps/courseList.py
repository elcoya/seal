from behave import *
from selenium import webdriver 

@when('we enter in the courser list')
def step(context):
    a = context.browser.find_element_by_link_text('Courses')
    a.click()

@then('we should see "{text}"')
def step(context, text):
    courseCounter = context.browser.find_elements_by_class_name('paginator')
    textCounter = courseCounter.
    assert textCounter == text

@given('I am in the course list page "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)

@when('course "{course}" exists')
def setp(context, course):
    a = context.browser.find_element_by_link_text('course')
    assert True;
