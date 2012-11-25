'''
Created on 08/11/2012

@author: anibal
'''
from seal.model.student import Student
from seal.model.teacher import Teacher
from django.contrib.auth.models import User

Teacher.objects.all().delete()
Student.objects.all().delete()
User.objects.exclude(username='seal').delete()

uid = 'teacher'
user = User()
user.username = uid
user.set_password(uid)
user.email = uid + "@foo.foo"
user.save()
teacher = Teacher()
teacher.user = user
teacher.name = uid
teacher.uid = uid
teacher.email = uid + "@foo.foo"
teacher.save()

uid = 'student'
user = User()
user.username = uid
user.set_password(uid)
user.email = uid + "@foo.foo"
user.save()
student = Student()
student.user = user
student.name = uid
student.uid = uid
student.email = uid + "@foo.foo"
student.save()

