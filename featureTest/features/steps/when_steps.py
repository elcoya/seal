from behave import *
from selenium import webdriver 
from seal.model import Course, Student, Practice

import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('../conf/local.cfg'))
pathproject = config.get("Path", "path.project")
filePath = pathproject + "featureTest/data/pdftest.pdf"
deliveryPath = pathproject + "featureTest/data/delivery.zip"

@when('I log in as "{usr}" "{passwd}"')
def step(context, usr, passwd):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('username').send_keys(usr)
    form.find_element_by_name('password').send_keys(passwd)
    form.submit()

@when('I input login data "{loginData}"')
def step(context, loginData):
    form = context.browser.find_element_by_tag_name('form')
    splitted = loginData.split('|')
    form.find_element_by_name('username').send_keys(splitted[0])
    form.find_element_by_name('password').send_keys(splitted[1])
    form.submit()

@when('I enter in the course list')
def step(context):
    a = context.browser.find_element_by_link_text('Courses')
    a.click()

@when('I enter in the "{idstudent}" home page')
def step(context, idstudent):
    student = Student.objects.get(uid=idstudent)
    url="http://localhost:8000/students/home/"+str(student.pk)
    context.browser.get(url)

@when('I fill the newstudent form with default data')
def step(context):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('name').send_keys('Dummy Student')
    form.find_element_by_name('uid').send_keys('00000')
    form.find_element_by_name('email').send_keys('dummy@foo.foo')
    form.find_element_by_name('courses').send_keys('2012-1')
    
@when('I submit the form')
def step(context):
    form = context.browser.find_element_by_tag_name('form')
    form.submit()
    
@when('I click in the "{text}" link')
def step(context, text):
    a = context.browser.find_element_by_link_text(text)
    a.click()
    
@when(u'I am at the new practice form')
def step(context):
    context.browser.get('http://localhost:8000/practices/newpractice')

@when(u'I fill the practice form with uid "{practice_uid}" and default data for course "{course_name}"')
def step(context, practice_uid, course_name):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('uid').send_keys(practice_uid)
    form.find_element_by_name('course').send_keys(course_name)
    form.find_element_by_name('file').send_keys(filePath)
    form.find_element_by_name('deadline').send_keys('2012-11-25')

@when('I fill the delivery form with default data')
def step(context):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('file').send_keys(deliveryPath)

@when('I am in the upload page of student "{student}" and practice "{practice}"')
def step(context,student,practice):
    p = Practice.objects.get(uid=practice)
    s = Student.objects.get(name=student)
    addres = 'http://localhost:8000/delivery/newdelivery/'+str(p.pk)+'/'+str(s.pk)
    context.browser.get(addres)
      
@when('I change "{course1}" for "{course2}" in element whith id "{idelement}"')
def step(context, course1, course2, idelement):
    form = context.browser.find_element_by_tag_name('form')
    context.browser.find_element_by_id(idelement).clear()
    form.find_element_by_id(idelement).send_keys(course2)
    
@when('I am in the modifier page of course "{course}"')
def step(context,course):
    c = Course.objects.get(name=course)
    addres = 'http://localhost:8000/course/editcourse/'+str(c.pk)
    context.browser.get(addres)

@when('I fill in the registration form with user "{uid}"')
def step(context, uid):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('name').send_keys(uid)
    form.find_element_by_name('uid').send_keys(uid)
    form.find_element_by_name('passwd').send_keys('seal')
    form.find_element_by_name('email').send_keys('foo@foo.foo')

@when('I am in the delivery page of student "{student}" and practice "{practice}"')
def step(context,student,practice):
    s = Student.objects.get(uid=student)
    p = Practice.objects.get(uid=practice)
    addres = 'http://localhost:8000/delivery/newdelivery/'+str(p.pk)+'/'+str(s.pk)
    context.browser.get(addres)
