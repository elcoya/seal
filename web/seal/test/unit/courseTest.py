from django.test import TestCase
from seal.model.course import Course

class CourseTest(TestCase):
    def testCourseToStringWhenInputInName20122CreturnString20122C(self):
        """
        Tests __str__
        """
        name = "20122C"
        course = Course()
        course.name = name
        assert_name = str(course)
        self.assertEqual(assert_name, name, "Course to string expected to be " + name + " but was " + assert_name)
    