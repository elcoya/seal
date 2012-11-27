'''
Created on 14/11/2012

@author: martin
'''

from django.test import TestCase
from seal.model import Suscription

class SuscriptionTest(TestCase):
    def testSuscriptionModelDescription(self):
        pk = 1
        suscription = Suscription()
        suscription.pk = pk
        assert_pk = str(suscription)
        self.assertEqual(assert_pk, str(pk), "Suscription to string expected to be " + str(pk) + " but was " + assert_pk)
