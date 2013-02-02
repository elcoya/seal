'''
Created on 11/12/2012

@author: anibal
'''
from auto_correction.preparation.prepare_files_strategy_zip import PrepareFilesStrategyZip
import shutil
import os
import subprocess
from auto_correction.log.logger_manager import LoggerManager

class SetupEnviroment():

    def __init__(self):
        self.prepare_files_strategy = PrepareFilesStrategyZip()
        self.log = LoggerManager().get_new_logger("setup enviroment")
    
    def run(self, automatic_correction, working_dir):
        self.log.debug("setting up enviroment...")
        self.log.debug("cleaning up working directory...")
        shutil.rmtree(working_dir, ignore_errors=True)
        self.log.debug("preparing delivery files...")
        self.prepare_files_strategy.zip = automatic_correction.delivery.file.name
        os.mkdir(working_dir)
        self.prepare_files_strategy.prepare_files(working_dir)
        shutil.copy(automatic_correction.delivery.practice.get_script().file.name, 
                    working_dir + "/" + os.path.basename(automatic_correction.delivery.practice.get_script().file.name))
        # We must ensure the script is runnable
        process = subprocess.Popen(["chmod", "a+x", working_dir + "/" + os.path.basename(automatic_correction.delivery.practice.get_script().file.name)])
        process.wait()
        self.log.debug("enviroment set.")
        
