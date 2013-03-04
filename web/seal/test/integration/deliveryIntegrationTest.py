"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Course, Delivery, Student, Practice

class DeliveryIntegrationTest(TestCase):
    def setUp(self):
        nameCourse = '2012-2'
        course = Course()
        course.name = nameCourse
        course.save()
        
        student = Student()
        student.uid = "85000"
        student.save()
        
        practice = Practice()
        practice.uid = "Tp inicial"
        practice.course = course
        practice.file = "pathFile"
        practice.deadline = "2012-12-01" 
        practice.save()
     
    def test_delivery_creation_compare_pk(self):
        student = Student.objects.get(uid="85000")
        practice = Practice.objects.get(uid="Tp inicial")
        
        p_delivery = Delivery()
        p_delivery.file = "pathFile"
        p_delivery.student = student
        p_delivery.practice = practice
        p_delivery.deliverDate = '2012-11-30'
        p_delivery.save()
        
        c_delivery = Delivery.objects.get(student=student, practice=practice)
        self.assertEqual(p_delivery.pk, c_delivery.pk)
    
    def tearDown(self):
        Delivery.objects.filter(file="pathFile", deliverDate="2012-11-30").delete()
        student = Student.objects.get(uid="85000")
        student.delete()
        practice = Practice.objects.get(uid="Tp inicial")
        practice.delete()
        p_course = Course.objects.get(name='2012-2')
        p_course.delete()