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
    
    TMP_DIR = "tmp_dir"
    
    def get_pending_autochecks(self):
        pending_autochecks = Autocheck.objects.filter(status=0)
        return self.filter_autochecks(pending_autochecks)
    
    def filter_autochecks(self, autochecks):
        
        return autochecks
    
    def move_delivery_zip_to_assigned_dir(self, delivery):
        return
    
    def setup_enviroment(self, delivery, script):
        shutil.rmtree(AutocheckRunner.TMP_DIR, ignore_errors=True)
        os.mkdir(AutocheckRunner.TMP_DIR)
        shutil.copy(delivery.file.name, AutocheckRunner.TMP_DIR + "/" + os.path.basename(delivery.file.name))
        zipfile = ZipFile(AutocheckRunner.TMP_DIR + "/" + os.path.basename(delivery.file.name))
        zipfile.extractall(AutocheckRunner.TMP_DIR)
        shutil.copy(script.file.name, AutocheckRunner.TMP_DIR + "/" + os.path.basename(script.file.name))
    
    def run_script(self, autocheck=None, script=None):
        script_file_name = AutocheckRunner.TMP_DIR + "/" + os.path.basename(script.file.name)
        process = subprocess.Popen(["chmod", "a+x", script_file_name])
        process.wait()
        process = subprocess.Popen([script_file_name], shell=False, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        exit_value = process.wait()
        output = process.communicate()
        captured_stdout = output[0]
        autocheck.exit_value = exit_value
        autocheck.captured_stdout = captured_stdout
        autocheck.status = 1 + (-2 * exit_value)
        return {"exit_value" : exit_value, "captured_stdout" : captured_stdout}
    
    def clean_up_tmp_dir(self):
        shutil.rmtree(AutocheckRunner.TMP_DIR, ignore_errors=True)
    
    def run(self):
        """Runs the corresponding script for every Delivery which has not yet been run."""
        
        results = {"successfull" : 0, "failed" : 0}
        pending_autochecks = self.get_pending_autochecks()
        for pending_autocheck in pending_autochecks:
            delivery = pending_autocheck.delivery
            practice = delivery.practice
            if (practice.script_set.all()):
                script = practice.script_set.all()[0]
                self.setup_enviroment(delivery, script)
                script_result = self.run_script(pending_autocheck, script)
                self.clean_up_tmp_dir()
                if(script_result["exit_value"] == 0):
                    results["successfull"] += 1
                else :
                    results["failed"] += 1
                pending_autocheck.save()
        return results;
    
