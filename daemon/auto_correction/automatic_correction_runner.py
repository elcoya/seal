import shutil
from execution.run_script_command import RunScriptCommand
from publication.publish_results_visitor_web import PublishResultsVisitorWeb
from auto_correction.preparation.setup_enviroment import SetupEnviroment
from auto_correction.utils import managepath
from auto_correction.selection.automatic_correction_selection_strategy_through_rest_api import AutomaticCorrectionSelectionStrategyThroughRestApi
from auto_correction.publication.publish_results_visitor_mail import PublishResultsVisitorMail
import os
from auto_correction.settings import REST_BASE_URL
from auto_correction.result.script_result import ScriptResult
from auto_correction.utils.dir_utils import walk_directory
from auto_correction.log.logger_manager import LoggerManager

HTTP_SERIALIZER = REST_BASE_URL + '/automaticcorrectionserializer/'
SERIALIZER_AUTH_USER = 'seal'
SERIALIZER_AUTH_PASS = 'seal'

class AutomaticCorrectionRunner():
    """
    
    This class is intended to be in charge of running the automated check on the
    queued deliveries from the seal.model application model. It is thought to be
    called in order to run the automatic correction script file for each delivery which has
    not yet been checked, and for the Practices which has a script.
    
    """
    
    TMP_DIR = managepath.get_instance().get_automatic_correction_tmp_dir()
    SUCCESSFULL_RESULTS_KEY = "successfull"
    FAILED_RESULTS_KEY = "failed"
    
    def __init__(self):
        self.selection_strategy = AutomaticCorrectionSelectionStrategyThroughRestApi(SERIALIZER_AUTH_USER, SERIALIZER_AUTH_PASS)
        self.setup_enviroment = SetupEnviroment()
        self.run_script_command = RunScriptCommand()
        self.publish_result_visitors = (PublishResultsVisitorWeb(SERIALIZER_AUTH_USER, SERIALIZER_AUTH_PASS), 
                                        PublishResultsVisitorMail(SERIALIZER_AUTH_USER, SERIALIZER_AUTH_PASS),)
        self.log = LoggerManager().get_new_logger("outer process")
    
    def clean_up_tmp_dir(self):
        shutil.rmtree(AutomaticCorrectionRunner.TMP_DIR, ignore_errors=True)
    
    def run(self):
        """Runs the corresponding script for every Delivery which has not yet been run."""
        
        results = {AutomaticCorrectionRunner.SUCCESSFULL_RESULTS_KEY : 0, AutomaticCorrectionRunner.FAILED_RESULTS_KEY : 0}
        pending_automatic_corrections = self.selection_strategy.get_automatic_corrections()
        for pending_automatic_correction in pending_automatic_corrections:
            
            try:
                self.setup_enviroment.run(pending_automatic_correction, AutomaticCorrectionRunner.TMP_DIR)
                self.log.info("Walking tmp directory...")
                files_list = []
                walk_directory(files_list, AutomaticCorrectionRunner.TMP_DIR, "")
                for item in files_list:
                    self.log.info(" - " + item)
                
                self.run_script_command.set_script(os.path.join(AutomaticCorrectionRunner.TMP_DIR, os.path.basename(pending_automatic_correction.script)))
                script_result = self.run_script_command.execute()
            except Exception, e:
                script_result = ScriptResult()
                script_result.captured_stdout = "An error has occurred while running the automatic correction process. Error information: " + str(e)
                script_result.exit_value = 2
                
            script_result.automatic_correction = pending_automatic_correction
            for visitor in self.publish_result_visitors:
                script_result.accept(visitor)
            self.clean_up_tmp_dir()
            if(script_result.exit_value == 0):
                results[AutomaticCorrectionRunner.SUCCESSFULL_RESULTS_KEY] += 1
            else :
                results[AutomaticCorrectionRunner.FAILED_RESULTS_KEY] += 1
        return results;
    
