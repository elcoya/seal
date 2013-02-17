import subprocess
from auto_correction.exceptions.illegal_state_exception import IllegalStateException
from auto_correction.result.script_result import ScriptResult
from auto_correction.log.logger_manager import LoggerManager
from auto_correction.execution.run_script_timeout import ProcessTimeout

class RunScriptCommand():
    """
    
    Top class for the hierarchy of the Command in charge of running the scripts
    of autocorrection for Practices. This should ONLY run the script and 
    capture the results, so that they can be published afterwards when the
    visitors in the 'publication' package are run.
    
    """
    
    TIME_OUT = 5 # seconds
    
    def __init__(self):
        self.script = None
        self.log = LoggerManager().get_new_logger("run script")
    
    def set_script(self, script):
        self.script = script
    
    def execute(self):
        if(self.script is None):
            self.log.error("attempt to run the correction process but the script to be run is not defined.")
            raise IllegalStateException(reason="In order to execute the script, you must set it first.")
        # now we may call the script
        self.log.debug("launching correction process...")
        process = subprocess.Popen([self.script], shell=False, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        # must ensure that the process won't run forever
        process_timer = ProcessTimeout(process, RunScriptCommand.TIME_OUT)
        process_timer.start_timer()
        self.log.debug("Process timeout timer launched")
        # finally, we must capture all results so the can be published
        script_result = ScriptResult()
        self.log.debug("waiting for process to finish...")
        script_result.exit_value = process.wait()
        self.log.debug("process finished with exit value %d", script_result.exit_value)
        #if the result has been obtained, the is no point on keeping the timer alive
        if process_timer.ran:
            self.log.info("Execution has been terminated for exceding the timeout limit.")
        else:
            process_timer.cancel_timer()
            self.log.debug("Process finished correctly without exceding timeout limit.")
        
        output = process.communicate()
        script_result.captured_stdout = output[0]
        self.log.debug("stdout captured.")
        self.log.debug("excecution completed.")
        return script_result
