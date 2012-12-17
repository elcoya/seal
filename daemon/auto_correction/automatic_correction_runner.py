import shutil
from selection.automatic_correction_selection_strategy_pending_and_runnable import AutomaticCorrectionSelectionStrategyPendingAndRunnable
from execution.run_script_command import RunScriptCommand
from publication.publish_results_visitor_web import PublishResultsVisitorWeb
from auto_correction.preparation.setup_enviroment import SetupEnviroment
from celery import task

class AutomaticCorrectionRunner():
    """
    
    This class is intended to be in charge of running the automated check on the
    queued deliveries from the seal.model application model. It is thought to be
    called in order to run the automatic correction script file for each delivery which has
    not yet been checked, and for the Practices which has a script.
    
    """
    
    TMP_DIR = "/tmp/tmp_dir"
    
    def __init__(self):
        self.selection_strategy = AutomaticCorrectionSelectionStrategyPendingAndRunnable()
        self.setup_enviroment = SetupEnviroment()
        self.run_script_command = RunScriptCommand()
        self.publish_result_visitors = (PublishResultsVisitorWeb(), )
    
    def clean_up_tmp_dir(self):
        shutil.rmtree(AutomaticCorrectionRunner.TMP_DIR, ignore_errors=True)
    
    def run(self):
        """Runs the corresponding script for every Delivery which has not yet been run."""
        
        results = {"successfull" : 0, "failed" : 0}
        pending_automatic_corrections = self.selection_strategy.get_automatic_corrections()
        for pending_automatic_correction in pending_automatic_corrections:
            
            self.setup_enviroment.run(pending_automatic_correction, AutomaticCorrectionRunner.TMP_DIR)
            self.run_script_command.set_script(pending_automatic_correction.delivery.practice.get_script().file.name)
            script_result = self.run_script_command.execute()
            script_result.automatic_correction = pending_automatic_correction
            for visitor in self.publish_result_visitors:
                script_result.accept(visitor)
            
            self.clean_up_tmp_dir()
            if(script_result.exit_value == 0):
                results["successfull"] += 1
            else :
                results["failed"] += 1
        return results;
    
