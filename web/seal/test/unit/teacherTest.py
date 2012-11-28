from django.test import TestCase
from seal.model import Teacher

class TeacherTest(TestCase):

    def testTeacherToStringInputteacherReturnteacher(self):
        name = "teacher"
        teacher = Teacher()
        teacher.name = name
        self.assertEqual(str(teacher), name)