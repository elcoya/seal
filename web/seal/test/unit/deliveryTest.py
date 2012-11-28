"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Delivery, Student, Practice, Course

class DeliveryTest(TestCase):
    def setUp(self):
        course = Course.objects.create(name = "2012-1", pk = 1)
        self.student = Student.objects.create(name = "Nombre y Apellido")
        self.practice = Practice.objects.create(uid = "Tp inicial", course = course, deadline = '2012-11-25') 
        
    def testDeliveryToStringReturnNamePracticeNameStudentAndDeadLinePractice(self):    
        deadline = "2012-11-25"
        str_practice_return = "Tp inicial - Nombre y Apellido - 2012-11-25"
        delivery = Delivery()
        delivery.student = self.student
        delivery.practice = self.practice
        delivery.deliverDate = deadline
        self.assertEqual(str(delivery), str_practice_return)