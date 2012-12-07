"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Delivery, Student, Practice

class DeliveryTest(TestCase):
    def setUp(self):
        self.student = Student()
        self.student.name = "Nombre y Apellido"
        self.practice = Practice()
        self.practice.uid = "Tp inicial"
    
    def testDeliveryToStringReturnNamePracticeNameStudentAndDeadLinePractice(self):    
        deliveryDate = "2012-11-25"
        str_practice_return = "Tp inicial - Nombre y Apellido - 2012-11-25"
        delivery = Delivery()
        
        print isinstance(self.student, Student)
        print isinstance(self.practice, Practice)
        
        delivery.student = self.student
        delivery.practice = self.practice
        delivery.deliverDate = deliveryDate
            
        self.assertEqual(str(delivery), str_practice_return)