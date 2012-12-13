'''
Created on 07/12/2012

@author: anibal
'''
import unittest
from auto_correction.selection.automatic_correction_selection_strategy_pending_and_runnable import AutomaticCorrectionSelectionStrategyPendingAndRunnable
from mock import Mock


class TestAutomaticCorrectionSelectionStrategy(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def testAutomaticCorrectionSelectionStrategyShouldInvokeAutomaticCorrectionFilterMethod(self):
        # FIXME: the selection strategy uses AutomaticCorrection.objects, and that is not 'mockable'. This is an alternative action.
        automatic_correction_selection_strategy = AutomaticCorrectionSelectionStrategyPendingAndRunnable()
        automatic_correction_selection_strategy.object_manager = Mock()
        automatic_correction_selection_strategy.list_filter = Mock()
        
        automatic_correction_selection_strategy.get_automatic_corrections()
        
        automatic_correction_selection_strategy.object_manager.filter.assert_called_with(status=0)
        automatic_correction_selection_strategy.list_filter.filter.assert_any_call()
