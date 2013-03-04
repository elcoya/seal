'''
Created on 07/12/2012

@author: anibal
'''
import unittest
from mock import Mock
from auto_correction.selection.automatic_correction_selection_strategy_through_rest_api import AutomaticCorrectionSelectionStrategyThroughRestApi


class TestAutomaticCorrectionSelectionStrategy(unittest.TestCase):
    
    def testAutomaticCorrectionSelectionStrategyShouldInvokeRestApiHelperMethod(self):
        user = Mock()
        password = Mock()
        rest_api_helper = Mock()
        return_value = (Mock(),)
        rest_api_helper.get_automatic_corrections.return_value = return_value
        automatic_correction_selection_strategy = AutomaticCorrectionSelectionStrategyThroughRestApi(user, password)
        automatic_correction_selection_strategy.rest_api_helper = rest_api_helper
        
        actual_return_value = automatic_correction_selection_strategy.get_automatic_corrections()
        
        self.assertEqual(actual_return_value, return_value)
        rest_api_helper.get_automatic_corrections.assert_called()


