"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Practice, Course

class PracticeTest(TestCase):
    
    def setUp(self):
        nameCourse = '2012-2'
        course = Course()
        course.name = nameCourse
        course.save()
    
    def testPracticeModelDescription(self):
        practice = Practice()
        practice.uid = "practice_uid"
        self.assertEqual(str(practice), "practice_uid")
    
    def testPracticeCreation(self):
        pCourse = Course.objects.get(name='2012-2')
        pPractice = Practice()
        pPractice.uid = "1"
        pPractice.course = pCourse
        pPractice.file = "pathFile"
        pPractice.deadline = "2012-12-01" 
        pPractice.save()
        cPractice = Practice.objects.get(uid="1")
        self.assertEqual(pPractice.course.name, cPractice.course.name)
    
    def tearDown(self):
        Practice.objects.filter(uid="1").delete()
        pCourse = Course.objects.get(name='2012-2')
        pCourse.delete()