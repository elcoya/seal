from django.test import TestCase
from seal.model.course import Course
from seal.model.student import Student
from seal.model.shift import Shift

class CourseTest(TestCase):
    
    def setUp(self):
        Student.objects.all().delete()
    
    def testCourseToStringWhenInputInName20122CreturnString20122C(self):
        name = "20122C"
        course = Course()
        course.name = name
        self.assertEqual(str(course), name)
    
