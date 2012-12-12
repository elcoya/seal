import subprocess
from auto_correction.exceptions.illegal_state_exception import IllegalStateException
from auto_correction.result.script_result import ScriptResult

class RunScriptCommand():
    """
    
    Top class for the hierarchy of the Command in charge of running the scripts
    of autocorrection for Practices. This should ONLY run the script and 
    capture the results, so that they can be published afterwards when the
    visitors in the 'publication' package are run.
    
    """
    
    def __init__(self):
        self.script = None
    
    def set_script(self, script):
        self.script = script
    
    def execute(self):
        if(self.script is None):
            raise IllegalStateException(reason="In order to execute the script, you must set it first.")
        # now we may call the script
        process = subprocess.Popen([self.script], shell=False, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        # finally, we must capture all results so the can be published
        script_result = ScriptResult()
        script_result.exit_value = process.wait()
        output = process.communicate()
        script_result.captured_stdout = output[0]
        return script_result
