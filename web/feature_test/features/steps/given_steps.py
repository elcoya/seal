from behave import *
from selenium import webdriver
from seal.model import Course, Practice, Delivery, Correction
from seal.model.student import Student
from django.template.defaulttags import now
from django.contrib.auth.models import User
from django.contrib.auth import logout
from seal.model.teacher import Teacher
from string import capitalize
from seal.forms import student
from seal.model.suscription import Suscription
from seal.model.script import Script
from seal.model.automatic_correction import AutomaticCorrection
from seal.model.practice_file import PracticeFile
from seal.utils import managepath
import os
from shutil import copyfile
from os import makedirs

base_url = 'http://localhost:8000/'

@given('I have opened the browser for "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)

@given('Teacher "{username}" exists with password "{password}"')
def step(context, username, password):
    if(Teacher.objects.filter(uid=username).exists()):
        teacher = Teacher.objects.get(uid=username)
        teacher.user.set_password(password)
        teacher.user.save()
        teacher.save()
    else:
        teacher = Teacher()
        teacher.uid = username
        user = User()
        user.username = username
        user.first_name = username
        user.last_name = username
        user.set_password(password)
        user.email = username + "@foo.foo"
        user.save()
        teacher.user = user
        teacher.save()

@given('Student "{username}" exists with password "{password}"')
def step(context, username, password):
    if(Student.objects.filter(uid=username).exists()):
        student = Student.objects.get(uid=username)
        student.user.set_password(password)
        student.user.save()
        student.save()
    else:
        student = Student()
        student.uid = username
        user = User()
        user.username = username
        user.first_name = username
        user.last_name = username
        user.set_password(password)
        user.email = username + "@foo.foo"
        user.save()
        student.user = user
        student.save()

@given('Student "{username}" exists with email "{email}"')
def step(context, username, email):
    if(Student.objects.filter(uid=username).exists()):
        student = Student.objects.get(uid=username)
        student.user.set_password(username)
        student.user.save()
        student.save()
    else:
        student = Student()
        student.uid = username
        user = User()
        user.username = username
        user.first_name = username
        user.last_name = username
        user.set_password(username)
        user.email = email
        user.save()
        student.user = user
        student.save()

@given('I log in as "{usr}" "{passwd}"')
def step(context, usr, passwd):
    if(context.browser.find_elements_by_link_text('logout')):
        a = context.browser.find_element_by_link_text('logout')
        a.click()
    elif(context.browser.find_elements_by_link_text('Log out')):
        a = context.browser.find_element_by_link_text('Log out')
        a.click()
    else:
        context.browser.get(base_url)
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('username').send_keys(usr)
    form.find_element_by_name('password').send_keys(passwd)
    form.submit()

@given('I am in the index page')
def step(context):
    context.browser.get(base_url)

@given('I am in the practice list page')
def step(context):
    context.browser.get(base_url + 'teacher/practices/')

@given('I am at the new student form')
def step(context):
    context.browser.get(base_url + 'teacher/students/newstudent')

@given('there are no courses')
def step(context):
    Course.objects.all().delete()

@given('there are no practices')
def step(context):
    Practice.objects.all().delete()

@given('there are no students')
def step(context):
    Student.objects.all().delete()

@given('there are no deliveries')
def step(context):
    Delivery.objects.all().delete()

@given('there are no corrections')
def step(context):
    Correction.objects.all().delete()

@given('there are no suscription')
def step(context):
    Suscription.objects.all().delete()

@given('course "{course}" exists')
def step(context,course):
    c = Course.objects.get_or_create(name=course)

@given('student "{uid}" exists in course "{course1}" and in course "{course2}"')
def step(context,uid, course1, course2):
    course1 = Course.objects.get(name=course1)
    course2 = Course.objects.get(name=course2)
    student = Student.objects.get(uid=uid)
    student.courses.add(course1)
    student.courses.add(course2)

@given('student "{uid}" exists in course "{course}"')
def step(context,uid, course):
    course = Course.objects.get(name=course)
    student = Student.objects.get(uid=uid)
    student.courses.add(course)

@given('student "{uid}" does not exist in course "{course}"')
def step(context,uid, course):
    course = Course.objects.get(name=course)
    if(course.get_students(uid=uid).exists()):
        course.get_students().remove(uid=uid)

@given('student "{uid}" exists without course')
def step(context,uid):
    student = Student.objects.get(uid=uid)
    student.courses.clear()

@given('there are no student in "{course}"')
def step(context, course):
    c = Course.objects.get(name=course)
    students = c.get_students()
    for student in students:
        student.delete()

@given('there are no practices in course "{course}"')
def step(context, course):
    c = Course.objects.get(name=course)
    practices = c.get_practices()
    for practice in practices:
        practice.delete()
        
@given('practice "{practice_uid}" exists in course "{course_name}" with deadline "{dead_line}"')
def step (context, practice_uid, course_name, dead_line):
    c = Course.objects.get(name=course_name)
    if(Practice.objects.filter(uid=practice_uid).exists()):
        Practice.objects.get(uid=practice_uid).delete()
    practice = Practice()
    practice.uid = practice_uid
    practice.deadline = dead_line
    practice.course = c
    practice.save()

@given('I am at the new practice form for course "{namecourse}"')
def step(context,namecourse):
    c = Course.objects.get(name=namecourse)
    path = base_url + "teacher/practices/newpractice/" + str(c.pk)
    context.browser.get(path)

@given('I am not logged in')
def step(context):
    assert True

@given('user "{uid}" is not registered')
def step(context, uid):
    if(Student.objects.filter(uid=uid).exists()):
        student = Student.objects.get(uid=uid)
        student.user.delete()
        student.delete()

@given('user "{uid}" is registered')
def step(context, uid):
    if((Student.objects.filter(uid=uid).exists()) is False):
        if(User.objects.filter(username=uid).exists()):
            User.objects.get(username=uid).delete()
        user = User()
        user.username = uid
        user.set_password("seal")
        user.email = "foo@foo.foo"
        user.save()
        student = Student()
        student.user = user
        student.uid = uid
        student.save()

@given('exist delivery of "{practice}" from student "{student}" whit dalivery date "{deliveryDate}"')
def step(context,practice,student,deliveryDate):
    s = Student.objects.get(uid=student)
    p = Practice.objects.get(uid=practice)
    Delivery.objects.get_or_create(file="archivo.zip",student_id=s.pk,practice_id=p.pk, deliverDate=deliveryDate)

@given('exist correction of delivery of "{student}" for "{practice}" with "{coment1}" "{coment2}" "{grade}" and corrector "{corrector}"')
def step(context,practice,student,coment1,coment2,grade,corrector):
    s = Student.objects.get(uid=student)
    p = Practice.objects.get(uid=practice)
    d = Delivery.objects.get(student=s, practice=p)
    t = Teacher.objects.get(uid=corrector)
    Correction.objects.get_or_create(publicComent=coment1,privateComent=coment2,grade=grade,delivery_id=d.pk,corrector_id=t.pk)

@given('existe suscrition of student "{student}" for course "{course}" with suscription date "{suscriptionDate}" and state "{state}"')
def step(context,student,course,suscriptionDate,state):
    s = Student.objects.get(uid=student)
    c = Course.objects.get(name=course)
    Suscription.objects.get_or_create(student_id=s.pk, course_id=c.pk, state=state, suscriptionDate=suscriptionDate)

@given('I am at the upload script form for practice "{practice_uid}" and course "{course_name}"')
def step(context, practice_uid, course_name):
    course = Course.objects.get(name=course_name)
    practice = Practice.objects.get(uid=practice_uid, course=course)
    path = base_url + "teacher/practices/script/" + str(course.pk) + "/" + str(practice.pk)
    context.browser.get(path)
    
@given(u'script "{script_name}" is set for practice "{practice_uid}" for course "{course_name}"')
def impl(context, script_name, practice_uid, course_name):
    course = Course.objects.get(name=course_name)
    practice = Practice.objects.get(uid=practice_uid, course=course)
    practice.delete_script()
    script = Script()
    script.file="data/"+script_name
    script.practice = practice
    script.save()

@given(u'a delivery exists for practice "{practice_uid}" and course "{course_name}" from Student "{student_uid}" with id "{delivery_id}"')
def step(context, practice_uid, course_name, student_uid, delivery_id):
    student = Student.objects.get(uid=student_uid)
    course = Course.objects.get(name=course_name)
    practice = Practice.objects.get(uid=practice_uid, course=course)
    # delivery = Delivery.objects.get_or_create(pk=delivery_id, student=student, practice=practice)
    delivery = Delivery()
    delivery.pk = delivery_id
    src = "data/delivery.zip"
    delivery_path = managepath.get_instance().get_delivery_path()
    dst = os.path.join(delivery_path, "delivery.zip")
    if(not os.path.exists(delivery_path)):
        makedirs(delivery_path)
    if(not os.path.exists(dst)):
        copyfile(src, dst)
    delivery.file = dst
    delivery.student = student
    delivery.practice = practice
    delivery.deliverDate = '2012-11-22'
    delivery.save()
    automatic_correction = AutomaticCorrection()
    automatic_correction.delivery = delivery
    automatic_correction.save()


@given(u'a delivery exists for practice "{practice_uid}" and course "{course_name}" from Student "{student_uid}"')
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

@given('file "{filename}" existe in the practice "{practice_uid}" and course "{course_name}"')
def step(context, practice_uid, course_name, filename):
    course = Course.objects.get(name=course_name)
    practice = Practice.objects.get(uid=practice_uid, course=course)
    practiceFile = PracticeFile()
    practiceFile.name = filename
    practiceFile.file = "data/file.pdf"
    practiceFile.practice = practice
    practiceFile.save()
    
@given(u'automatic_correction for all deliveries has status "{str_status}"')
def step(context, str_status):
    automatic_corrections = AutomaticCorrection.objects.all()
    status_map = {"successfull": 1, "failed": -1, "pending": 0}
    status = status_map[str_status]
    for automatic_correction in automatic_corrections:
        automatic_correction.status = status
        automatic_correction.save()

@given(u'automatic_correction for all deliveries has exit_value "{exit_value}"')
def step(context, exit_value):
    automatic_corrections = AutomaticCorrection.objects.all()
    value = int(exit_value)
    for automatic_correction in automatic_corrections:
        automatic_correction.exit_value = value
        automatic_correction.save()

@given(u'automatic_correction for all deliveries has stdout "{stdout}"')
def step(context, stdout):
    automatic_correction = AutomaticCorrection.objects.all()
    for automatic_correction in automatic_correction:
        automatic_correction.captured_stdout = stdout
        automatic_correction.save()

@given(u'Teacher "{teacher}" is the corrector of student "{student}"')
def step(context, teacher, student):
    t = Teacher.objects.get(uid=teacher)
    s = Student.objects.get(uid=student)
    s.corrector = t
    s.save()

@given(u'text file is bound to practice "{practice_name}" with id "{practice_file_id}"')
def step(context, practice_name, practice_file_id):
    practice_path = managepath.get_instance().get_practice_path()
    if not os.path.exists(practice_path):
        os.makedirs(name=practice_path)
    practice_filename = "practice_text_file.txt"
    practice_filepath = os.path.join(practice_path, practice_filename)
    with open(practice_filepath, 'w') as test_file:
        lines = ["first line\n",
                 "second line\n",
                 "third line\n",
                 "fourth line\n",
                 "fifth line\n"]
        test_file.writelines(lines)
    practice = Practice.objects.filter(uid=practice_name)[0]
    practice_file = PracticeFile()
    practice_file.pk = practice_file_id
    practice_file.name = "Prueba"
    practice_file.file = practice_filepath
    practice_file.practice = practice
    practice_file.save()
    

@given(u'not text file is bound to practice "{practice_name}" with id "{practice_file_id}"')
def step(context, practice_name, practice_file_id):
    practice_path = managepath.get_instance().get_practice_path()
    if not os.path.exists(practice_path):
        os.makedirs(name=practice_path)
    practice_filename = "practice_not_text_file.pdf"
    practice_filepath = os.path.join(practice_path, practice_filename)
    with open(practice_filepath, 'w') as test_file:
        lines = ["first line\n",
                 "second line\n",
                 "third line\n",
                 "fourth line\n",
                 "fifth line\n"]
        test_file.writelines(lines)
    practice = Practice.objects.filter(uid=practice_name)[0]
    practice_file = PracticeFile()
    practice_file.pk = practice_file_id
    practice_file.name = "Prueba"
    practice_file.file = practice_filepath
    practice_file.practice = practice
    practice_file.save()


