from seal.model.autocheck import Autocheck
from seal.model.delivery import Delivery
from zipfile import ZipFile
import os
import shutil
import subprocess

class AutocheckRunner():
    """
    
    This class is intended to be in charge of running the automated check on the
    queued deliveries from the seal.model application model. It is thought to be
    called in order to run the autocheck script file for each delivery which has
    not yet been checked, and for the Practices which has a script.
    
    """

    def run(self):
        """
        
        Runs the corresponding script for every Delivery which has not yet been
        run.
        
        """
        
        results = {"successfull" : 0, "failed" : 0}
        pending_autochecks = Autocheck.objects.filter(status=0)
        for pending_autocheck in pending_autochecks:
            delivery = pending_autocheck.delivery
            practice = delivery.practice
            if (practice.script_set.all()):
                script = practice.script_set.all()[0]
                script_result = self.run_script(pending_autocheck, script)
                pending_autocheck.exit_value = script_result["exit_value"]
                pending_autocheck.captured_stdout += script_result["captured_stdout"]
                if(script_result["exit_value"] == 0):
                    pending_autocheck.status = 1 #successfull
                    results["successfull"] += 1
                else :
                    pending_autocheck.status = -1 #failed
                    results["failed"] += 1
                pending_autocheck.save()
        return results;
    
    def run_script(self, autocheck=None, script=None):
        tmp_dir = "tmp_zip"
        script_file_name = os.path.basename(script.file.name)
        zipfile = ZipFile(autocheck.delivery.file)
        shutil.rmtree(tmp_dir, ignore_errors=True)
        os.mkdir(tmp_dir)
        zipfile.extractall(tmp_dir)
        self.copy(script.file.name, tmp_dir + "/" + script_file_name)
        process = subprocess.Popen(["chmod", "a+x", tmp_dir + "/" + script_file_name])
        process.wait()
        process = subprocess.Popen([tmp_dir + "/" + script_file_name], shell=False, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        exit_value = process.wait()
        output = process.communicate()
        captured_stdout = output[0]
        
        shutil.rmtree(tmp_dir, ignore_errors=True)
        return {"exit_value" : exit_value, "captured_stdout" : captured_stdout}
    
    def copy(self, from_path, to_path):
        shutil.copyfile(from_path, to_path)
