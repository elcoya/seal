"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import PracticeFile

class PracticeFileTest(TestCase):
    def testPracticeFileToStringReturnNamePutForTheTeacher(self):
        name = "Enunciado"
        practice_file = PracticeFile()
        practice_file.name = name
        self.assertEqual(str(practice_file), name)
    
    def testEditableFunctionReturnTrueWhenIPutATextFile(self):
        filename = "file.txt"
        practice_file = PracticeFile()
        practice_file.file = filename
        self.assertTrue(practice_file.isEditable(), "Error is Editable")
        
    def testEditableFunctionReturnFalseWhenIPutANotTextFile(self):
        filename = "file.pdf"
        practice_file = PracticeFile()
        practice_file.file = filename
        self.assertFalse(practice_file.isEditable(), "Error is Editable")
    