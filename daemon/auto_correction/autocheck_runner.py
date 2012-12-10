import os
import shutil
from daemon.selection.autocheck_selection_strategy_pending_and_runnable import AutocheckSelectionStrategyPendingAndRunnable
from daemon.preparation.prepare_files_strategy_zip import PrepareFilesStrategyZip
from daemon.execution.run_script_command import RunScriptCommand
from daemon.publication.publish_results_visitor_web import PublishResultsVisitorWeb

class AutocheckRunner():
    """
    
    This class is intended to be in charge of running the automated check on the
    queued deliveries from the seal.model application model. It is thought to be
    called in order to run the autocheck script file for each delivery which has
    not yet been checked, and for the Practices which has a script.
    
    """
    
    TMP_DIR = "tmp_dir"
    
    def __init__(self):
        self.selection_strategy = AutocheckSelectionStrategyPendingAndRunnable()
        self.prepare_files_strategy = PrepareFilesStrategyZip()
        self.run_script_command = RunScriptCommand()
        self.publish_result_visitors = (PublishResultsVisitorWeb(), )
    
    def setup_enviroment(self, delivery, script):
        shutil.rmtree(AutocheckRunner.TMP_DIR, ignore_errors=True)
        self.prepare_files_strategy.zip = delivery.file.name
        self.prepare_files_strategy.prepare_files(AutocheckRunner.TMP_DIR)
        shutil.copy(script.file.name, AutocheckRunner.TMP_DIR + "/" + os.path.basename(script.file.name))
    
    def clean_up_tmp_dir(self):
        shutil.rmtree(AutocheckRunner.TMP_DIR, ignore_errors=True)
    
    def run(self):
        """Runs the corresponding script for every Delivery which has not yet been run."""
        
        results = {"successfull" : 0, "failed" : 0}
        pending_autochecks = self.selection_strategy.get_autochecks()
        for pending_autocheck in pending_autochecks:
            delivery = pending_autocheck.delivery
            practice = delivery.practice
            # FIXME: the selection strategy should get only the autochecks for practices with associated autochecks
            if (practice.script_set.all()):
                script = practice.script_set.all()[0]
                self.setup_enviroment(delivery, script)
                self.run_script_command.set_script(script)
                script_result = self.run_script_command.execute()
                for visitor in self.publish_result_visitors:
                    script_result.accept(visitor)
                
                self.clean_up_tmp_dir()
                if(script_result.exit_value == 0):
                    results["successfull"] += 1
                else :
                    results["failed"] += 1
        return results;
    
