from auto_correction.execution.run_script_command import RunScriptCommand
from auto_correction.exceptions.illegal_state_exception import IllegalStateException
from unittest.case import TestCase
import subprocess
import os

class TestRunScriptCommand(TestCase):

    script_file_path = "/tmp/"
    script_file_name = "successfull_test_script.sh"
    
    def setUp(self):
        self.heading = "#!/bin/bash\n"
        self.text = "This is the successfull script\n"
        self.body = "echo " + self.text
        self.exit = "exit 0\n"
        f = open(self.script_file_path + self.script_file_name, "w")
        f.writelines((self.heading, self.body, self.exit,));
        f.close()
        # We must ensure the script is runnable
        process = subprocess.Popen(["chmod", "a+x", self.script_file_path + self.script_file_name])
        process.wait()
    
    def testRunScriptCommandMustRunTheScriptAndEndSuccessfully(self):
        runner = RunScriptCommand()
        runner.set_script(os.path.join(self.script_file_path, self.script_file_name))
        result = runner.execute()
        self.assertEquals(result.exit_value, 0)
        self.assertEquals(result.captured_stdout, self.text)
        
    def testRunScriptCommandShouldRiseIllegalStateExceptionIfCalledBeforeSettingScript(self):
        runner = RunScriptCommand()
        with self.assertRaises(IllegalStateException):
            runner.execute()
        