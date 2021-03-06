import shutil
from auto_correction.preparation.prepare_files_strategy_zip import PrepareFilesStrategyZip
from auto_correction.exceptions.illegal_state_exception import IllegalStateException
from unittest.case import TestCase

import ConfigParser, os
from auto_correction.utils import managepath

import errno

class TestPrepareFilesStrategy(TestCase):
    
    DAEMON_BASE_PATH = managepath.get_instance().get_daemon_path()      # Required to use the app model
    INPUT_DATA_FILES_PATH = managepath.get_instance().get_base_proyect_path() + "web/feature_test/data/"

    UNZIP_DESTINATION_PATH = DAEMON_BASE_PATH + "test_tmp/unzip/"
    ZIP_FILE_PATH = DAEMON_BASE_PATH +"test_tmp/delivery.zip"
    ORIGINAL_ZIP_FILE_PATH = INPUT_DATA_FILES_PATH + "delivery.zip"
    ZIPPED_FILE_NAME = "prueba.txt"
    

    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise
    
    def setUp(self):
        self.mkdir_p(TestPrepareFilesStrategy.UNZIP_DESTINATION_PATH)
        self.mkdir_p(os.path.dirname(TestPrepareFilesStrategy.ZIP_FILE_PATH))
        shutil.copy(TestPrepareFilesStrategy.ORIGINAL_ZIP_FILE_PATH, TestPrepareFilesStrategy.ZIP_FILE_PATH)
    
    def tearDown(self):
        shutil.rmtree(TestPrepareFilesStrategy.UNZIP_DESTINATION_PATH, ignore_errors=True)
        shutil.rmtree(os.path.dirname(TestPrepareFilesStrategy.ZIP_FILE_PATH), ignore_errors=True)
    
    def testPrepareFilesStrategyZipShouldUnpackTheZipFileAssociatedWithTheDeliveryToTheGivenPath(self):
        strategy = PrepareFilesStrategyZip()
        strategy.zip = TestPrepareFilesStrategy.ZIP_FILE_PATH
        strategy.prepare_files(TestPrepareFilesStrategy.UNZIP_DESTINATION_PATH)
        self.assertTrue(os.path.exists(TestPrepareFilesStrategy.UNZIP_DESTINATION_PATH + TestPrepareFilesStrategy.ZIPPED_FILE_NAME))
    
    def testPrepareFilesStrategyZipShouldRiseIllegalStateExceptionIfCalledWithoutSettingTheSourceFile(self):
        strategy = PrepareFilesStrategyZip()
        with self.assertRaises(IllegalStateException):
            strategy.prepare_files(TestPrepareFilesStrategy.UNZIP_DESTINATION_PATH)
        