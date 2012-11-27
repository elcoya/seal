from django.test import TestCase
from django.contrib.auth.models import User
from seal.model import Teacher

class TeacherTest(TestCase):

    def testTeacherModelDescription(self):
        """
        Tests __str__
        """
        name = "teacher"
        teacher = Teacher()
        teacher.name = name
        assert_name = str(teacher)
        self.assertEqual(assert_name, name, "Teacher to string expected to be " + name + " but was " + assert_name)