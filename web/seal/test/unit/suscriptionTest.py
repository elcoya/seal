'''
Created on 14/11/2012

@author: martin
'''

from django.test import TestCase
from seal.model import Suscription

class SuscriptionTest(TestCase):
    def testSuscriptionToStringInsterPk1return1(self):
        pk = 1
        suscription = Suscription()
        suscription.pk = pk
        self.assertEqual(str(suscription), str(pk))
