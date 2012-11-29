from django.test import TestCase
from seal.model.autocheck import Autocheck
from seal.test.integration.utils import clean_up_database_tables,\
    create_a_course, create_a_student, create_a_practice, create_a_delivery,\
    create_an_autocheck, load_a_script
from daemon.autocheck_runner import AutocheckRunner
from seal.settings import project_base_path
from seal.model.script import Script
from seal.model.delivery import Delivery
from seal.model.practice import Practice
from seal.model.course import Course

class TestAutocheckRunner(TestCase):

    course_name = "2012-2"
    student_name = "student"
    student_email = "student@foo.foo"
    practice_deadline = '2012-12-31'
    practice_filepath = "practice_filepath"
    practice_uid = "practice_uid"
    script_file = "successfull_test_script.sh"
    delivery_filepath = "delivery.zip"
    delivery_date = '2012-12-15'
    stdout = "some generated stdout"
    exit_value = 0
    status = 0

    def setUp(self):
        clean_up_database_tables()
        create_a_course(self.course_name)
        create_a_student(self.student_name, self.student_email, self.course_name)
        create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        load_a_script(self.course_name, self.practice_uid, self.script_file)
        create_a_delivery(self.delivery_filepath, self.student_name, self.course_name, self.practice_uid, self.delivery_date)
        create_an_autocheck(self.delivery_filepath, self.stdout, self.exit_value, self.status)


    def tearDown(self):
        clean_up_database_tables()


    def testTheMethodMustReturnOnlyOneElementInTheList(self):
        runner = AutocheckRunner()
        pending_autochecks = runner.get_pending_autochecks()
        self.assertEquals(len(pending_autochecks), 1)
    
    def testRunScriptMustTurnPendingAutocheckToSuccessfull(self):
        runner = AutocheckRunner()
        course = Course.objects.get(name=self.course_name)
        practice = Practice.objects.get(course=course, uid=self.practice_uid)
        script = Script.objects.get(practice=practice)
        delivery = Delivery.objects.get(file=self.delivery_filepath)
        autocheck = Autocheck.objects.get(delivery=delivery)
        runner.run_script(autocheck, script)
        self.assertEquals(autocheck.status, 1)
