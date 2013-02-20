from seal.test.integration.utils import clean_up_database_tables,\
    create_a_course, create_a_student, create_a_practice, create_a_delivery,\
    create_an_automatic_correction, load_a_script
from auto_correction.automatic_correction_runner import AutomaticCorrectionRunner
import os
from zipfile import ZipFile
from unittest.case import TestCase

class TestAutomaticCorrectionRunner(TestCase):

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
        clean_up_database_tables()
        self.course = create_a_course(self.course_name)
        self.student = create_a_student(self.student_name, self.student_email, self.course_name)
        self.practice = create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        self.script = load_a_script(self.course_name, self.practice_uid, self.script_file)
        self.delivery = create_a_delivery(self.delivery_filepath, self.student_name, self.course_name, self.practice_uid, self.delivery_date)
        self.automatic_correction = create_an_automatic_correction(self.delivery_filepath, self.stdout, self.exit_value, self.status)

    def tearDown(self):
        clean_up_database_tables()

    def testTheMethodMustReturnOnlyOneElementInTheList(self):
        runner = AutomaticCorrectionRunner()
        pending_automatic_corrections = runner.get_pending_automatic_corrections()
        self.assertEquals(len(pending_automatic_corrections), 1)

    def testAutomaticCorrectionRunnerMustCreateDirectoryToRunScript(self):
        runner = AutomaticCorrectionRunner()
        runner.setup_enviroment(self.delivery, self.script)
        self.assertTrue(os.path.isfile(AutomaticCorrectionRunner.TMP_DIR + "/" + os.path.basename(self.script.file.name)))
        zipfile = ZipFile(self.delivery.file.name)
        for name in zipfile.namelist():
            self.assertTrue(os.path.isfile(AutomaticCorrectionRunner.TMP_DIR + "/" + name))
    
    def testAutomaticCorrectionRunnerMustCleanUpDirectoryAfterRunningScript(self):
        runner = AutomaticCorrectionRunner()
        runner.clean_up_tmp_dir()
        self.assertFalse(os.path.isfile(AutomaticCorrectionRunner.TMP_DIR + "/" + os.path.basename(self.script.file.name)))
    
    def testRunScriptMustTurnPendingAutomaticCorrectionToSuccessfull(self):
        runner = AutomaticCorrectionRunner()
        runner.setup_enviroment(self.delivery, self.script)
        runner.run_script(self.automatic_correction, self.script)
        runner.clean_up_tmp_dir()
        self.assertEquals(self.automatic_correction.status, 1)
        
