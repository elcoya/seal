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
    
    def testStudentCreation(self):
        pStudent = Student()
        pStudent.name = "Nombre y Apellido"
        pStudent.uid = '85000'
        pStudent.email = "email@pagnia.com.ar"
        pStudent.save()
        cStudent = Student.objects.get(uid='85000')
        self.assertEqual(pStudent.uid, cStudent.uid)
        
    def testStudenteEqualUid(self):
        pStudent = Student()
        p1Student = Student()
        
        pStudent.name = "Nombre y Apellido"
        pStudent.uid = "50000"
        pStudent.email = "email@pagnia.com.ar"
        #save de first estudent...
        pStudent.save()
        
        p1Student.name = "Nombre y Apellido"
        p1Student.uid = "50000"
        p1Student.email = "email@pagnia.com.ar"
        try:
            #try save second student withd equal uid 
            p1Student.save()
            assert(False)
        except Exception:
            self.assert_("exceptions.BaseException", Exception.message)
