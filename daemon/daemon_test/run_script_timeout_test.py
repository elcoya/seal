"""
@author: anibal
"""
import unittest
from mock import Mock
from auto_correction.execution.run_script_timeout import ProcessTimeout


class TestProcessTimeout(unittest.TestCase):

    def testStartTimerShouldInvokeStartMethodTimer(self):
        process = Mock()
        timer = Mock()
        process_timeout = ProcessTimeout(process, 1000)
        process_timeout.timer = timer
        
        process_timeout.start_timer()
        
        timer.start.assert_called()
    
    def testCancelTimerShouldInvokeCancelMethodTimer(self):
        process = Mock()
        timer = Mock()
        process_timeout = ProcessTimeout(process, 1000)
        process_timeout.timer = timer
        
        process_timeout.cancel_timer()
        
        timer.cancel.assert_called()
    
    def testKillProcShouldInvokeKillOnTheTimeoutedProcess(self):
        process = Mock()
        timer = Mock()
        process_timeout = ProcessTimeout(process, 1000)
        process_timeout.timer = timer
        
        process_timeout.kill_proc()
        
        process.kill.assert_called()


