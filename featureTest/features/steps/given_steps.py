from behave import *
from selenium import webdriver
from django.core.exceptions import ObjectDoesNotExist
from seal.model import Course, Practice
from seal.model.student import Student

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
    print(context)
    context.browser.get('http://localhost:8000/admin/model/course/')

@given('I am in the practice list page')
def step(context):
    print(context)
    context.browser.get('http://localhost:8000/practices/')

@given('I am at the new student form')
def step(context):
    context.browser.get('http://localhost:8000/students/newstudent')

@given('there are no courses')
def step(context):
    Course.objects.all().delete()

@given('there are no practices')
def step(context):
    Practice.objects.all().delete()

@given('there are no students')
def step(context):
    Student.objects.all().delete()

@given('course "{course}" exists')
def step(context,course):
    try:
        c = Course.objects.get(name=course)
    except ObjectDoesNotExist:
        assert False 

