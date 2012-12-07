from daemon.result.script_result import ScriptResult
from daemon.publication.publish_results_visitor_web import PublishResultsVisitorWeb
from unittest.case import TestCase
from mock import Mock
from seal.model.autocheck import Autocheck

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
        self.autocheck = Mock(spec=Autocheck) # create_an_autocheck(self.delivery_filepath, self.stdout, self.exit_value, self.status)
        self.script_result = ScriptResult()
        self.script_result.autocheck = self.autocheck
        self.script_result.exit_value = self.exit_value
        self.script_result.captured_stdout = self.stdout
    
    def tearDown(self):
        pass
    
    def testTheVisitorShouldSaveTheModificationsToTheDatabaseSoThatTheResultsWillBeReflectedOnTheWebsite(self):
        publish_result_visitor_web = PublishResultsVisitorWeb()
        self.script_result.accept(publish_result_visitor_web)
        self.assertEqual(self.autocheck.exit_value, 0)
        self.assertEqual(self.autocheck.captured_stdout, self.stdout)
        self.assertEqual(self.autocheck.status, 1)
        self.autocheck.save.assert_called()
    
    def testTheVisitorShouldInvokeTheEmailSendingProcessForTheVisitedResult(self):
        pass
