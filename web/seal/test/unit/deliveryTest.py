"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Delivery, Student, Practice

class DeliveryTest(TestCase):
    def testDeliveryModelDescription(self):
        delivery = Delivery()
        delivery.student = Student.objects.get(uid='85000')
        delivery.practice = Practice.objects.get(uid="Tp inicial")
        delivery.deliverDate = '2012-11-25'
        self.assertEqual(str(delivery), "Tp inicial - Nombre y Apellido - 2012-11-25")