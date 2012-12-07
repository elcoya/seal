'''
Created on 07/12/2012

@author: anibal
'''
import unittest
from daemon.selection.autocheck_selection_strategy_pending_and_runnable import AutocheckSelectionStrategyPendingAndRunnable
from mock import Mock


class TestAutocheckSelectionStrategy(unittest.TestCase):

    def setUp(self):
        pass
    
    def testAutocheckSelectionStrategyShouldInvokeAutocheckFilterMethod(self):
        # FIXME: the selection strategy uses Autocheck.objects, and that is not 'mockable'. This is an alternative action.
        autocheck_selection_strategy = AutocheckSelectionStrategyPendingAndRunnable()
        autocheck_selection_strategy.object_manager = Mock()
        autocheck_selection_strategy.get_autochecks()
        autocheck_selection_strategy.object_manager.filter.assert_called_with(status=0)
    