from behave import *
from selenium import webdriver 

@given('we have opened the browser for "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)