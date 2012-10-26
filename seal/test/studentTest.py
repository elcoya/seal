"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Student,Course

class StudentTest(TestCase):
    
    def setUp(self):
        nameCourse = '2012-1'
        course = Course()
        course.name = nameCourse
        course.save()
                
    def testStudentCreation(self):
        sCourse = Course.objects.get(name='2012-1')
        pStudent = Student()
        pStudent.name = "Nombre y Apellido"
        pStudent.uid = 85000
        pStudent.email = "email@pagnia.com.ar"
        pStudent.course = sCourse
        pStudent.save()
        cStudent = Student.objects.get(uid=85000)
        self.assertEqual(pStudent.uid, cStudent.uid)
        
    def testStudenteEqualUid(self):
        sCourse = Course.objects.get(name='2012-1')
        
        pStudent = Student()
        p1Student = Student()
        
        pStudent.name = "Nombre y Apellido"
        pStudent.uid = 50000
        pStudent.email = "email@pagnia.com.ar"
        pStudent.course = sCourse
        #save de first estudent...
        pStudent.save()
        
        p1Student.name = "Nombre y Apellido"
        p1Student.uid = 85000
        p1Student.email = "email@pagnia.com.ar"
        p1Student.course = sCourse
        
        try:
            #try save second student withd equal uid 
            p1Student.save()
            assert(False)
        except Exception:
            self.assert_("exceptions.BaseException", Exception.message)