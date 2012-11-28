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
        
    def testDeliveryModelDescription(self):    
        delivery = Delivery()
        delivery.student = self.student
        delivery.practice = self.practice
        delivery.deliverDate = '2012-11-25'
        self.assertEqual(str(delivery), "Tp inicial - Nombre y Apellido - 2012-11-25")