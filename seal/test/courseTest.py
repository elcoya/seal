from django.test import TestCase
from seal.model.course import Course

class CourseTest(TestCase):
    def testCourseCreation(self):
        """
        We creates a Course with a name and checks it's value.
        """
        aName = '2012-2C'
        aCourse = Course()
        aCourse.name = aName
        self.assertEqual(aCourse.name, aName)