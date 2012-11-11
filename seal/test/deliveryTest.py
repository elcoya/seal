"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Course, Delivery, Student, Practice
from django.db.models.sql.datastructures import Date

class DeliveryTest(TestCase):
    def setUp(self):
        nameCourse = '2012-2'
        course = Course()
        course.name = nameCourse
        course.save()
        
        student = Student()
        student.name = "Nombre y Apellido"
        student.uid = "85000"
        student.email = "email@pagnia.com.ar"
        student.save()
        
        practice = Practice()
        practice.uid = "Tp inicial"
        practice.course = course
        practice.file = "pathFile"
        practice.deadline = "2012-12-01" 
        practice.save()
        
        
    def testPracticeCreation(self):
        student = Student.objects.get(uid="85000")
        practice = Practice.objects.get(uid="Tp inicial")
        
        pDelivery = Delivery()
        pDelivery.file = "pathFile"
        pDelivery.student = student
        pDelivery.practice = practice
        pDelivery.deliverDate = '2012-11-30'
        pDelivery.save()
        
        cDelivery = pDelivery.objects.get(uid=1)
        self.assertEqual(pDelivery.pk, cDelivery.pk)
    
    def tearDown(self):
        delivery = Delivery.objects.get(uid=1)
        delivery.delete()
        student = Student.objects.get(uid="85000")
        student.delete()
        practice = Practice.objects.get(uid="Tp inicial")
        practice.delete()
        pCourse = Course.objects.get(name='2012-2')
        pCourse.delete()