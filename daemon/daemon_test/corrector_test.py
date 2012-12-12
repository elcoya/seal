import unittest
from auto_correction.autocheck_runner import AutocheckRunner
from mock import Mock
from auto_correction.result.script_result import ScriptResult

class CorrectorTest(unittest.TestCase):


    def testEjecutarDeberiaConsultarCorreccionesPendientes(self):
        corrector = AutocheckRunner()
        selection_strategy_mock = Mock()
        selection_strategy_mock.get_autochecks.return_value = list()
        corrector.selection_strategy = selection_strategy_mock
        
        corrector.run()
        
        corrector.selection_strategy.get_autochecks.assert_called()
        
    def testEjecutarDeberiaInvocarAlCorregirCuandoHayCorreccionesPendientes(self):
        corrector = AutocheckRunner()
        autocheck = Mock()
        selection_strategy_mock = Mock()
        selection_strategy_mock.get_autochecks.return_value = (autocheck, )
        setup_enviroment_mock = Mock()
        script_result = ScriptResult()
        script_result.exit_value = 0
        script_result.captured_stdout = "some stdout"
        execution_command_mock = Mock()
        execution_command_mock.execute.return_value = script_result
        
        publication_visitor = Mock()
        
        corrector.selection_strategy = selection_strategy_mock
        corrector.setup_enviroment = setup_enviroment_mock
        corrector.run_script_command = execution_command_mock
        corrector.publish_result_visitors = (publication_visitor, )
        
        corrector.run()
        
        selection_strategy_mock.get_autochecks.assert_called()
        setup_enviroment_mock.setup_enviroment.assert_called()
        execution_command_mock.execute.assert_called()
        publication_visitor.visit.assert_called()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()