"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Student

class StudentTest(TestCase):
    
    def testStudentToStringInputNameReturnName(self):
        name = "Name"
        student = Student()
        student.name = name
        self.assertEqual(str(student), name)