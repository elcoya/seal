from auto_correction.result.script_result import ScriptResult
from auto_correction.publication.publish_results_visitor_web import PublishResultsVisitorWeb
from unittest.case import TestCase
from mock import Mock
from seal.model.automatic_correction import AutomaticCorrection
from auto_correction.publication.publish_results_visitor_mail import PublishResultsVisitorMail

class PublishResultVisitorTest(TestCase):

    student = None
    practice = None
    course = None
    script = None
    delivery = None
    automatic_correction = None

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
        self.automatic_correction = Mock(spec=AutomaticCorrection)
        self.script_result = ScriptResult()
        self.script_result.automatic_correction = self.automatic_correction
        self.script_result.exit_value = self.exit_value
        self.script_result.captured_stdout = self.stdout
    
    def tearDown(self):
        pass
    
    def testTheVisitorShouldSaveTheModificationsToTheDatabaseSoThatTheResultsWillBeReflectedOnTheWebsite(self):
        user = Mock()
        password = Mock()
        publish_result_visitor_web = PublishResultsVisitorWeb(user, password)
        rest_api_helper = Mock()
        publish_result_visitor_web.rest_api_helper = rest_api_helper
        
        self.script_result.accept(publish_result_visitor_web)
        
        self.assertEqual(self.automatic_correction.exit_value, 0)
        self.assertEqual(self.automatic_correction.captured_stdout, self.stdout)
        self.assertEqual(self.automatic_correction.status, 1)
        self.automatic_correction.save.assert_called()
        rest_api_helper.save_automatic_correction.assert_called_with(self.automatic_correction)
    
    def testTheVisitorShouldInvokeTheEmailSendingProcessForTheVisitedResult(self):
        user = Mock()
        password = Mock()
        publish_result_visitor_mail = PublishResultsVisitorMail(user, password)
        rest_api_helper = Mock()
        publish_result_visitor_mail.rest_api_helper = rest_api_helper
        
        self.script_result.accept(publish_result_visitor_mail)
        
        rest_api_helper.save_mail.assert_called()
    
    