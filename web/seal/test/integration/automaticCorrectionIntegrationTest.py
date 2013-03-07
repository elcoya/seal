from django.test import TestCase
from seal.model.automatic_correction import AutomaticCorrection
from seal.model.delivery import Delivery
from seal.test.integration.utils import clean_up_database_tables, create_a_student, \
create_a_course, create_a_practice, create_a_delivery, create_an_automatic_correction,\
    create_a_inning

class AutomaticCorrectionIntegrationTest(TestCase):
    
    course_name = "2012-2"
    inning_name = "TARDE"
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
        create_a_inning(self.inning_name, self.course_name)
        create_a_student(self.student_name, self.inning_name)
        create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        create_a_delivery(self.delivery_filepath, self.student_name, self.course_name, self.practice_uid, self.delivery_date)
        create_an_automatic_correction(self.delivery_filepath, self.stdout, self.exit_value, self.status)
    
    def testAutomaticCorrectionCreation(self):
        delivery = Delivery.objects.get(file=self.delivery_filepath)
        automatic_correction = AutomaticCorrection.objects.get(delivery=delivery, exit_value=self.exit_value, status=self.status)
        self.assertEqual(automatic_correction.captured_stdout, self.stdout)
        self.assertEqual(automatic_correction.exit_value, self.exit_value)
        self.assertEqual(automatic_correction.status, self.status)
        self.assertEqual(automatic_correction.get_status( ), "pending")
