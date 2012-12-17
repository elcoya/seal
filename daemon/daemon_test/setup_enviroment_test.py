import shutil
from unittest.case import TestCase

import ConfigParser, os
from mock import Mock
from auto_correction.preparation.setup_enviroment import SetupEnviroment
config = ConfigParser.ConfigParser()
config.readfp(open(os.environ['PROJECT_PATH'] + 'daemon/conf/local.cfg'))

import errno

class TestSetupEnviroment(TestCase):
    
    DAEMON_BASE_PATH = config.get("Path", "path.project.daemon")      # Required to use the app model

    ORIGINAL_SCRIPT_FILE_PATH = DAEMON_BASE_PATH + "feature_test/data/"
    DESTINATION_PATH = DAEMON_BASE_PATH + "test_tmp/unzip/"
    SCRIPT_FILE_NAME = "successfull_test_script.sh"
    

    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise
    
    def setUp(self):
        self.mkdir_p(TestSetupEnviroment.DESTINATION_PATH)
    
    def tearDown(self):
        shutil.rmtree(TestSetupEnviroment.DESTINATION_PATH, ignore_errors=True)
    
    def testSetupEnviromentShouldCallThePrepareFilesStrategyAndCopyTheScriptFile(self):
        setup_enviroment = SetupEnviroment()
        strategy = Mock()
        setup_enviroment.prepare_files_strategy = strategy
        automatic_correction = Mock()
        return_value = Mock()
        return_value.file.name = TestSetupEnviroment.ORIGINAL_SCRIPT_FILE_PATH + TestSetupEnviroment.SCRIPT_FILE_NAME
        automatic_correction.delivery.practice.get_script.return_value = return_value
        
        setup_enviroment.run(automatic_correction, TestSetupEnviroment.DESTINATION_PATH)
        
        strategy.prepare_files.assert_called()
        self.assertTrue(os.path.exists(TestSetupEnviroment.DESTINATION_PATH + TestSetupEnviroment.SCRIPT_FILE_NAME))

