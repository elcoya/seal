from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from seal.model import Course, Student, Practice, Delivery, Suscription

import ConfigParser
from seal.model.automatic_correction import AutomaticCorrection
import time
from seal.utils import managepath

pathproject = managepath.get_instance().get_web_path()
filePath = pathproject + "feature_test/data/pdftest.pdf"
deliveryPath = pathproject + "feature_test/data/delivery.zip"
scriptPath = pathproject + "feature_test/data/"

base_url = 'http://localhost:8000/'

@when('I am in the index page')
def step(context):
    context.browser.get(base_url)

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

@when('I logout')
def step(context):
    a = context.browser.find_element_by_link_text('logout')
    a.click()

@when('I enter in the course list')
def step(context):
    a = context.browser.find_element_by_link_text('Courses')
    a.click()

@when('I fill the newstudent form with default data for course "{coursename}"')
def step(context, coursename):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('name').send_keys('Dummy Student')
    form.find_element_by_name('uid').send_keys('dummy')
    form.find_element_by_name('email').send_keys('dummy@foo.foo')
    form.find_element_by_name('courses').send_keys(coursename)
    form.find_element_by_name('passwd').send_keys('dummy')
    form.find_element_by_name('passwd_again').send_keys('dummy')

@when('I fill the upload file form with name "{namefile}"')
def step(context, namefile):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('name').send_keys(namefile)
    form.find_element_by_name('file').send_keys(filePath)
    
@when('I submit the form')
def step(context):
    form = context.browser.find_element_by_tag_name('form')
    form.submit()

@when('I click the link to "{link_text}"')
def step(context, link_text):
    links = context.browser.find_elements_by_tag_name('a')
    link_to_click = False
    for link in links:
        if (link_text in link.get_attribute("href")):
            link_to_click = link
            break
    link.click()

@when('I click in the "{text}" link')
def step(context, text):
    a = context.browser.find_element_by_link_text(text)
    a.click()
    
@when(u'I am at the new practice form')
def step(context):
    context.browser.get(base_url + 'teacher/practices/newpractice')

@when(u'I fill the practice form with uid "{practice_uid}" and default data for course "{course_name}"')
def step(context, practice_uid, course_name):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('uid').send_keys(practice_uid)
    form.find_element_by_name('course').send_keys(course_name)
    form.find_element_by_name('deadline').send_keys('2012-11-25')

@when('I fill the delivery form with default data')
def step(context):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('file').send_keys(deliveryPath)

@when('I am in the upload page of practice "{practice}"')
def step(context,practice):
    p = Practice.objects.get(uid=practice)
    addres = base_url + 'undergraduate/delivery/upload/'+str(p.pk)
    context.browser.get(addres)
      
@when('I change "{course1}" for "{course2}" in element whith id "{idelement}"')
def step(context, course1, course2, idelement):
    form = context.browser.find_element_by_tag_name('form')
    context.browser.find_element_by_id(idelement).clear()
    form.find_element_by_id(idelement).send_keys(course2)
    
@when('I am in the modifier page of course "{course}"')
def step(context,course):
    c = Course.objects.get(name=course)
    addres = base_url + 'teacher/course/editcourse/'+str(c.pk)
    context.browser.get(addres)

@when('I am in the suscription list page of course "{course}"')
def step(context,course):
    c = Course.objects.get(name=course)
    addres = base_url + 'teacher/suscription/list/'+str(c.pk)
    context.browser.get(addres)

@when('I fill in the registration form with user "{uid}"')
def step(context, uid):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('name').send_keys(uid)
    form.find_element_by_name('uid').send_keys(uid)
    form.find_element_by_name('passwd').send_keys('seal')
    form.find_element_by_name('passwd_again').send_keys('seal')
    form.find_element_by_name('email').send_keys('foo@foo.foo')

@when('I fill the recovery form with user "{uid}" and email "{email}"')
def step(context, uid, email):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('uid').send_keys(uid)
    form.find_element_by_name('email').send_keys(email)

@when('I fill the change password form with user "{uid}", oldpass "{oldpass}", newpass "{newpass}", newpassagin "{newpassagain}"')
def step(context, uid, oldpass, newpass, newpassagain):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('uid').send_keys(uid)
    form.find_element_by_name('oldpasswd').send_keys(oldpass)
    form.find_element_by_name('passwd').send_keys(newpass)
    form.find_element_by_name('passwd_again').send_keys(newpassagain)
    
@when('I am in the delivery page of practice "{practice}"')
def step(context,practice):
    p = Practice.objects.get(uid=practice)
    addres = base_url + 'undergraduate/delivery/upload/'+str(p.pk)
    context.browser.get(addres)

@when('I am in the list page of delivery from "{practice}"')
def step(context,practice):
    p = Practice.objects.get(uid=practice)
    addres = base_url + 'teacher/delivery/list/'+str(p.pk)
    context.browser.get(addres)

@when('I am in the correction delivery page of student "{student}" and practice "{practice}"')
def step(context,student,practice):
    s = Student.objects.get(uid=student)
    p = Practice.objects.get(uid=practice)
    d = Delivery.objects.get(student=s, practice=p)
    addres = base_url + 'teacher/correction/'+str(d.pk)
    context.browser.get(addres)

@when('I am at the explore delivery page for delivery "{id_delivery}"')
def step(context, id_delivery):
    address = base_url + 'teacher/delivery/explore/' + id_delivery
    context.browser.get(address)

@when(u'I am at the browse delivery page for delivery "{id_delivery}" browsing "{file_path}"')
def step(context, id_delivery, file_path):
    address = base_url + 'teacher/delivery/browse/' + id_delivery + "/" + file_path
    context.browser.get(address)


@when('I fill the form with "{coment1}" "{coment2}" "{grade}"')
def step(context, coment1, coment2, grade):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_id('id_publicComent').send_keys(coment1)
    form.find_element_by_id('id_privateComent').send_keys(coment2)
    form.find_element_by_name('grade').send_keys(grade)

@when('I am in the correction consult page of delivery from student "{student}" and practice "{practice}"')
def step(context,student,practice):
    s = Student.objects.get(uid=student)
    p = Practice.objects.get(uid=practice)
    d = Delivery.objects.get(student=s, practice=p)
    addres = base_url + 'undergraduate/correction/consult/'+str(d.pk)
    context.browser.get(addres)

@when('I check the suscription of student "{student}" for course "{course}"')
def step(context,student,course):
    s = Student.objects.get(uid=student)
    c = Course.objects.get(name=course)
    s = Suscription.objects.get(student=s, course=c)
    checkbox = context.browser.find_elements(By.ID, str(s.pk))
    checkbox[0].click()
    
@when('I click the button "{name}"')
def step(context, name):
    button = context.browser.find_elements(By.NAME, name)
    button[0].click()
    
@when('I click in the checkAll')
def step(context):
    checkbox = context.browser.find_elements(By.NAME, 'checkAll')
    checkbox[0].click()

@when('I fill in the upload script form with the file "{script_name}"')
def step(context, script_name):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('file').send_keys(scriptPath + script_name)

@when(u'I create a new delivery for practice "{practice_uid}" and course "{course_name}" from Student "{student_uid}"')
def step(context, practice_uid, course_name, student_uid):
    student = Student.objects.get(uid=student_uid)
    course = Course.objects.get(name=course_name)
    practice = Practice.objects.get(uid=practice_uid, course=course)
    delivery = Delivery()
    delivery.file = "data/delivery.zip"
    delivery.student = student
    delivery.practice = practice
    delivery.deliverDate = '2012-11-22'
    delivery.save()
    automatic_correction = AutomaticCorrection()
    automatic_correction.delivery = delivery
    automatic_correction.save()

@when('I select lenguaje "{lenguaje}"')
def step(context, lenguaje):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('language').send_keys(lenguaje)

@when('I select the corrector "{corrector}"')
def step(context, corrector):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('corrector').send_keys(corrector)

@when("I wait")
def step(context):
    time.sleep(5)

@when(u'I am at the list files page for practice "{practice_name}"')
def step(context, practice_name):
    practice = Practice.objects.get(uid=practice_name)
    address = base_url + 'teacher/practices/practicefile/' + str(practice.pk) + "/" + str(practice.pk)
    context.browser.get(address)

@when(u'I am at the edit text file page for practice "{practice_name}"')
def step(context, practice_name):
    practice = Practice.objects.get(uid=practice_name)
    practice_file = practice.get_practice_file()[0]
    address = base_url + 'teacher/practices/editfile/' + str(practice_file.pk)
    context.browser.get(address)

@when(u'I edit the practice text file in the form')
def step(context):
    textarea = context.browser.find_element_by_tag_name('textarea')
    textarea.send_keys("only line")

