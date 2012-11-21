from django.test import TestCase
from seal.model.autocheck import Autocheck
from seal.model.delivery import Delivery
from seal.test.utils import clean_up_database_tables, create_a_student, \
    create_a_course, create_a_practice, create_a_delivery, create_an_autocheck

class AutocheckTest(TestCase):
    
    course_name = "2012-2"
    student_name = "student"
    student_email = "student@foo.foo"
    practice_deadline = '2012-12-31'
    practice_filepath = "practice_filepath"
    practice_uid = "practice_uid"
    delivery_filepath = "delivery_filepath"
    delivery_date = '2012-12-15'
    stdout = "some generated stdout"
    exit_value = 0
    status = 0
    
    def setUp(self):
        clean_up_database_tables()
        create_a_course(self.course_name)
        create_a_student(self.student_name, self.student_email, self.course_name)
        create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        create_a_delivery(self.delivery_filepath, self.student_name, self.course_name, self.practice_uid, self.delivery_date)
        create_an_autocheck(self.delivery_filepath, self.stdout, self.exit_value, self.status)
    
    def testAutocheckCreation(self):
        delivery = Delivery.objects.get(file=self.delivery_filepath)
        autocheck = Autocheck.objects.get(delivery=delivery, exit_value=self.exit_value, status=self.status)
        self.assertEqual(autocheck.captured_stdout, self.stdout)
        self.assertEqual(autocheck.exit_value, self.exit_value)
        self.assertEqual(autocheck.status, self.status)
        self.assertEqual(autocheck.get_status( ), "pending")
