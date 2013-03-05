from django.test import TestCase
from django.contrib.auth.models import User
from seal.model import Teacher

class TeacherIntegrationTest(TestCase):
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
        
    def testCreationTeacherCompareUid(self):
        uid = "teacher"
        teacher = Teacher()
        teacher.uid = uid
        teacher.appointment = uid
        teacher.user = User.objects.get(username="test")
        teacher.save()
        c_teacher = Teacher.objects.get(uid=uid)
        self.assertEqual(c_teacher.uid, uid)
        
    def testCreationWithoutUserCatchException(self):
        msg = 'Teacher cannot be saved without an authentication register. Please, give the teacher an associated user so he can login.'
        name = "teacher"
        teacher = Teacher()
        teacher.iud = name
        try:
            teacher.save()
            assert(False)
        except Exception:
            self.assert_(msg, Exception.message)    
        
    def tearDown(self):
        User.objects.get(username="test").delete() 