"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Delivery, Student, Practice

class DeliveryTest(TestCase):
    def setUp(self):
        self.student = Student(name = "Nombre y Apellido")
        self.practice = Practice(uid = "Tp inicial", deadline = '2012-11-25') 
        
    def testDeliveryToStringReturnNamePracticeNameStudentAndDeadLinePractice(self):    
        deadline = "2012-11-25"
        str_practice_return = "Tp inicial - Nombre y Apellido - 2012-11-25"
        delivery = Delivery()
        delivery.student = self.student
        delivery.practice = self.practice
        delivery.deliverDate = deadline
        self.assertEqual(str(delivery), str_practice_return)