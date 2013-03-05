from django.test import TestCase
from seal.model import Teacher
from django.contrib.auth.models import User


class TeacherTest(TestCase):

    def testTeacherToStringInputteacherReturnteacher(self):
        uid = "teacher"
        teacher = Teacher()
        user = User()
        name = uid
        user.username = name
        user.first_name = name
        user.last_name = name
        user.email = "test@foo.foo"
        user.password = "pass"
        teacher.user = user
        self.assertEqual(str(teacher), uid)