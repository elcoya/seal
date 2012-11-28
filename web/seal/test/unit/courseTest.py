from django.test import TestCase
from seal.model.course import Course

class CourseTest(TestCase):
    def testCourseToStringWhenInputInName20122CreturnString20122C(self):
        name = "20122C"
        course = Course()
        course.name = name
        self.assertEqual(str(course), name)
    