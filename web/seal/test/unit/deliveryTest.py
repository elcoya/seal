"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Delivery, Student, Practice


class DeliveryTest(TestCase):
    def testDeliveryModelDescription(self):
        student = Student()
        student.name = "Nombre y Apellido"
        practice = Practice()
        practice.uid = "Tp inicial"
        
        delivery = Delivery()
        delivery.student = student
        delivery.practice = practice
        delivery.deliverDate = '2012-11-25'
        self.assertEqual(str(delivery), "Tp inicial - Nombre y Apellido - 2012-11-25")