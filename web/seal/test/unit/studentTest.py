"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Student

class StudentTest(TestCase):
    
    def testStudentToStringInputNameReturnName(self):
        uid = "uid"
        student = Student()
        student.uid = uid
        self.assertEqual(str(student), uid)