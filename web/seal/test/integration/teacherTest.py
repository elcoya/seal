from django.test import TestCase
from django.contrib.auth.models import User
from seal.model import Teacher

class TeacherTest(TestCase):
    def setUp(self):
        user = User()
        name = "test"
        user.username = name
        user.first_name = name
        user.last_name = name
        user.email = "test@foo.foo"
        user.password = "pass"
        user.is_staff = 1
        user.is_active = 1
        user.is_superuser = 0
        user.save()
        
    def testCreationTeacher(self):
        name = "teacher"
        teacher = Teacher()
        teacher.name = name
        teacher.iud = name
        teacher.email = "test@foo.foo"
        teacher.user = User.objects.get(username="test")
        teacher.save()
        c_teacher = Teacher.objects.get(name=name)
        self.assertEqual(c_teacher.name, name)
        
    def testCreationWithoutUser(self):
        msg = 'Teacher cannot be saved without an authentication register. Please, give the teacher an associated user so he can login.'
        name = "teacher"
        teacher = Teacher()
        teacher.name = name
        teacher.iud = name
        teacher.email = "test@foo.foo"
        try:
            teacher.save()
            assert(False)
        except Exception:
            self.assert_(msg, Exception.message)    
        
    def tearDown(self):
        User.objects.get(username="test").delete() 