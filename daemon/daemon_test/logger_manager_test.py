"""
@author: anibal
"""
import unittest
from mock import Mock
from auto_correction.log.logger_manager import LoggerManager
import logging


class LoggerManagerTest(unittest.TestCase):
    
    def testLoggerManagerMustReturnALoggerAppropiatelyConfiguredWhenProvidedAName(self):
        logger_manager = LoggerManager()
        logger = logger_manager.getLogger("a_name")
        pass
        #self.assertEquals(logger.__getattribute__('filename'), 'seal-daemon.log')
        
    def testLoggerManagerMustReturnALoggerAppropiatelyConfiguredWhenANameIsNotProvided(self):
        logger_manager = LoggerManager()
        logger = logger_manager.getLogger()
        pass

