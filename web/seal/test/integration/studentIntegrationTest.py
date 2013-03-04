"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Student

class StudentIntegrationTest(TestCase):

    def testStudentCreationCompareUid(self):
        pStudent = Student()
        pStudent.uid = '85000'
        pStudent.save()
        cStudent = Student.objects.get(uid='85000')
        self.assertEqual(pStudent.uid, cStudent.uid)
        
    def testStudenteEqualUid5000CatchBaseException(self):
        pStudent = Student()
        p1Student = Student()
        
        pStudent.uid = "50000"
        #save de first estudent...
        pStudent.save()
        
        p1Student.uid = "50000"
        try:
            #try save second student withd equal uid 
            p1Student.save()
            assert(False)
        except Exception:
            self.assert_("exceptions.BaseException", Exception.message)
