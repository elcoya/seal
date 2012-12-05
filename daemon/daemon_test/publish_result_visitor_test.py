from seal.test.integration.utils import clean_up_database_tables,\
    create_a_course, create_a_student, create_a_practice, create_a_delivery,\
    create_an_autocheck, load_a_script

from django.test import TestCase
from daemon.result.script_result import ScriptResult
from daemon.visitor.publish_results_visitor_web import PublishResultsVisitorWeb

class PublishResultVisitorTest(TestCase):

    student = None
    practice = None
    course = None
    script = None
    delivery = None
    autocheck = None

    course_name = "2012-2"
    student_name = "student"
    student_email = "student@foo.foo"
    practice_deadline = '2012-12-31'
    practice_filepath = "practice_filepath"
    practice_uid = "practice_uid"
    script_file = "/home/anibal/workspace/python-aptana-wkspace/seal/daemon/feature_test/data/successfull_test_script.sh"
    delivery_filepath = "/home/anibal/workspace/python-aptana-wkspace/seal/daemon/feature_test/data/delivery.zip"
    delivery_date = '2012-12-15'
    stdout = "some generated stdout"
    exit_value = 0
    status = 0
    
    
    def setUp(self):
        clean_up_database_tables()
        self.course = create_a_course(self.course_name)
        self.student = create_a_student(self.student_name, self.student_email, self.course_name)
        self.practice = create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        self.script = load_a_script(self.course_name, self.practice_uid, self.script_file)
        self.delivery = create_a_delivery(self.delivery_filepath, self.student_name, self.course_name, self.practice_uid, self.delivery_date)
        self.autocheck = create_an_autocheck(self.delivery_filepath, self.stdout, self.exit_value, self.status)
        self.script_result = ScriptResult()
        self.script_result.autocheck = self.autocheck
        self.script_result.exit_value = self.exit_value
        self.script_result.captured_stdout = self.stdout
    
    def tearDown(self):
        clean_up_database_tables()
    
    def testTheVisitorShouldSaveTheModificationsToTheDatabaseSoThatItWillBeReflectedOnTheWebsite(self):
        publish_result_visitor_web = PublishResultsVisitorWeb()
        self.script_result.accept(publish_result_visitor_web)
        self.assertEqual(self.autocheck.exit_value, 0)
        self.assertEqual(self.autocheck.captured_stdout, self.stdout)
        self.assertEqual(self.autocheck.status, 1)

