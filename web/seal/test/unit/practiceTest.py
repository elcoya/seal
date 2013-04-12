"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Practice

class PracticeTest(TestCase):
    def testPracticeToStringReturnPracticeUid(self):
        uid = "practice_uid"
        practice = Practice()
        practice.uid = uid
        self.assertEqual(str(practice), uid)
