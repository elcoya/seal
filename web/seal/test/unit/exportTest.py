"""
Created on 18/03/2013

@author: anibal
"""
from django.test import TestCase
from seal.model.student import Student
from seal.model.shift import Shift

class ExportLogicTest(TestCase):
    
    def testListCorrectionCommandShouldReturnTuplesWithInformationAboutDeliveriesMadeByStudents(self):
        shift1 = Shift
        student1 = Student.objects.get_or_create(uid='00000')
        
