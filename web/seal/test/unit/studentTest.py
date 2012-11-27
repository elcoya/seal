"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Student

class StudentTest(TestCase):
    
    def testStudentModelDescription(self):
        student = Student()
        student.name = "Nombre"
        self.assertEqual(str(student), "Nombre")