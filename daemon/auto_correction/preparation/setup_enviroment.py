'''
Created on 11/12/2012

@author: anibal
'''
from auto_correction.preparation.prepare_files_strategy_zip import PrepareFilesStrategyZip
import shutil
import os
import subprocess

class SetupEnviroment():

    def __init__(self):
        self.prepare_files_strategy = PrepareFilesStrategyZip()
    
    def run(self, autocheck, working_dir):
        shutil.rmtree(working_dir, ignore_errors=True)
        self.prepare_files_strategy.zip = autocheck.delivery.file.name
        self.prepare_files_strategy.prepare_files(working_dir)
        shutil.copy(autocheck.delivery.practice.script.file.name, working_dir + "/" + os.path.basename(autocheck.delivery.practice.get_script.file.name))
        # We must ensure the script is runnable
        process = subprocess.Popen(["chmod", "a+x", working_dir + "/" + os.path.basename(autocheck.delivery.practice.get_script().file.name)])
        process.wait()
        
