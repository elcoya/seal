"""
@author: anibal
"""
import unittest
from auto_correction.log.log import Log
from mock import Mock


class Test(unittest.TestCase):


    def testLog(self):
        logger_mock = Mock()
        message = "This is a test message and will not be actually logged anywhere"
        Log.LOGGER = logger_mock
        log = Log()
        
        log.debug(message)
        log.info(message)
        log.warning(message)
        log.error(message)
        log.critical(message)
        
        logger_mock.debug.assert_called_once_with(message)
        logger_mock.info.assert_called_once_with(message)
        logger_mock.warning.assert_called_once_with(message)
        logger_mock.error.assert_called_once_with(message)
        logger_mock.critical.assert_called_once_with(message)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLog']
    unittest.main()