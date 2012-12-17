'''
Created on 16/12/2012

@author: anibal
'''
import unittest
from auto_correction.daemon_control import LoopRunner
from mock import Mock


class Test(unittest.TestCase):


    def testLoopRunnerMustInvokeAutomaticCorrectionMethodRunWhileItsRunning(self):
        loop_runner = LoopRunner()
        automatic_correction_runner = Mock()
        loop_runner.automatic_correction_runner = automatic_correction_runner
        return_value = Mock()
        return_value.__str__.return_value = "mocking __str__()"
        loop_runner.automatic_correction_runner.run.return_value = return_value
        loop_interval = 1 # set this to 1 second so it doesn't wait too long
        loop_runner.loop_interval = loop_interval
        
        # FIXME: How do I test an endless loop??
        # loop_runner.run()
        
        automatic_correction_runner.run.assert_called()
        return_value.__str__.assert_called()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoopRunnerMustInvokeAutomaticCorrectionMethodRunWhileItsRunning']
    unittest.main()