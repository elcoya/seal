"""

General utility funtions grouped together to avoid code duplication

"""
from seal.model.autocheck import Autocheck
from seal.model.correction import Correction
from seal.model.delivery import Delivery
from seal.model.practice import Practice
from seal.model.suscription import Suscription
from seal.model.course import Course
from seal.model.student import Student
from seal.model.teacher import Teacher
from django.contrib.auth.models import User
from seal.model.script import Script

def clean_up_database_tables():
    Autocheck.objects.all().delete()
    Correction.objects.all().delete()
    Delivery.objects.all().delete()
    Practice.objects.all().delete()
    Suscription.objects.all().delete()
    Course.objects.all().delete()
    Student.objects.all().delete()
    Teacher.objects.all().delete()

def create_a_course(course_name):
    course = Course()
    course.name = course_name
    course.save()

def create_a_practice(course_name, practice_deadline, practice_filepath, practice_uid):
    practice = Practice()
    practice.course = Course.objects.get(name=course_name)
    practice.deadline = practice_deadline
    practice.file = practice_filepath
    practice.uid = practice_uid
    practice.save()

def get_user_for_student(student_name):
    user = User.objects.get_or_create(username=student_name)[0]
    user.set_password(student_name)
    user.save()
    return user

def create_a_student(student_name, student_email, course_name):
    student = Student()
    student.name = student_name
    student.uid = student_name
    student.email = student_email
    student.user = get_user_for_student(student_name)
    student.save()
    student.courses.add(Course.objects.get(name=course_name))
    student.save()

def load_a_script(course_name, practice_uid, script_file):
    course = Course.objects.get(name=course_name)
    practice = Practice.objects.get(course=course, uid=practice_uid)
    practice.script_set.all().delete()
    script = Script()
    script.practice = practice
    script.save()

def create_a_delivery(delivery_filepath, student_name, course_name, practice_uid, delivery_date):
    delivery = Delivery()
    delivery.file = delivery_filepath
    delivery.student = Student.objects.get(uid=student_name)
    course = Course.objects.get(name=course_name)
    delivery.practice = Practice.objects.get(course=course, uid=practice_uid)
    delivery.deliverDate = delivery_date
    delivery.save()

def create_an_autocheck(delivery_filepath, stdout, exit_value, status):
    autocheck = Autocheck()
    autocheck.delivery = Delivery.objects.get(file=delivery_filepath)
    autocheck.captured_stdout = stdout;
    autocheck.exit_value = exit_value
    autocheck.status = status
    autocheck.save()
