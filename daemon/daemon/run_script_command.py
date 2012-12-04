import subprocess
from exceptions.illegal_state_exception import IllegalStateException

class RunScriptCommand():
    """
    
    Top class for the hierarchy of the Command in charge of running the scripts
    of autocorrection for Practices. This should ONLY run the script and 
    capture the results, so that they can be published afterwards when the
    visitors are run.
    
    """
    
    KEY_EXIT_VALUE = "exit_value"
    KEY_CAPTURED_STDOUT = "captured_stdout"
    
    def __init__(self):
        self.script = None
    
    def set_script(self, script):
        self.script = script
    
    def excecute(self):
        if(self.script is None):
            raise IllegalStateException(reason="In order to excecute the script, you must set it first.")
        # We must ensure the script is runnable
        process = subprocess.Popen(["chmod", "a+x", self.script])
        process.wait()
        # now we may call the script
        process = subprocess.Popen([self.script], shell=False, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        # finally, we must capture all results so the can be published
        exit_value = process.wait()
        output = process.communicate()
        captured_stdout = output[0]
        return {RunScriptCommand.KEY_EXIT_VALUE : exit_value,
                RunScriptCommand.KEY_CAPTURED_STDOUT : captured_stdout}
