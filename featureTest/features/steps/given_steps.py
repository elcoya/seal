from behave import *
from selenium import webdriver
from django.core.exceptions import ObjectDoesNotExist
from seal.model import Course, Practice
from seal.model.student import Student
from django.template.defaulttags import now

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

@given('I am in the index page')
def step(context):
    print(context)
    context.browser.get('http://localhost:8000/')

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
        c = Course.objects.get_or_create(name=course)
    except ObjectDoesNotExist:
        assert False 

@given('practice "{practice_uid}" exists for course "{course_name}"')
def step(context, practice_uid, course_name):
    exists = Practice.objects.get(uid=practice_uid).exists()
    course = Course.objects.get_or_create(name=course_name)
    if(not exists):
        practice = Practice()
        practice.uid = practice_uid
        practice.deadline = now
        practice.file = '/tmp/selenium_test_file.pdf'
        practice.course = course
        practice.save()
    else:
        practice = Practice.objects.get(uid=practice_uid)
        if(practice.course is not course):
            practice.course = course
            practice.save()

@given(u'I am at the new practice form')
def step(context):
    context.browser.get('http://localhost:8000/practices/newpractice')
