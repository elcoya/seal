from behave import *
from selenium import webdriver

@given('I have opened the browser for "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)

@given('I log in as "{usr}" "{passwd}"')
def step(context, usr, passwd):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('username').send_keys(usr)
    form.find_element_by_name('password').send_keys(passwd)
    form.submit()

@given('I am in the course list page')
def step(context):
    print('need some help here...')
    print(context)
    context.browser.get('http://localhost:8000/admin/model/course/')

@given('there are no courses')
def step(context):
    courses = Courses.objects.all()
    for course in courses:
        course.delete()
