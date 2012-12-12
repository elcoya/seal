"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Practice, Course
from seal.model.script import Script

class PracticeIntegrationTest(TestCase):
    
    def setUp(self):
        nameCourse = '2012-2'
        self.course = Course()
        self.course.name = nameCourse
        self.course.save()
    
    def tearDown(self):
        Practice.objects.filter(uid="1").delete()
        pCourse = Course.objects.get(name='2012-2')
        pCourse.delete()
      
    def testPracticeCreationCompareName(self):
        pPractice = Practice()
        pPractice.uid = "1"
        pPractice.course = self.course
        pPractice.file = "pathFile"
        pPractice.deadline = "2012-12-01" 
        pPractice.save()
        cPractice = Practice.objects.get(uid="1")
        self.assertEqual(pPractice.course.name, cPractice.course.name)
    
    def testPracticeShouldFeatureSomeWrapperToAccessTheAssociatedScript(self):
        practice = Practice()
        practice.uid = "uid"
        practice.course = self.course
        practice.file = "pathFile"
        practice.deadline = "2012-12-01" 
        practice.save()
        script = Script()
        script.practice = practice
        script.save()
        self.assertEquals(practice.get_script(), script)
