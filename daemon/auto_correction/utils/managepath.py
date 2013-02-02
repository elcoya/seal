'''
Created on 30/01/2013

@author: martin
'''
import os

class Managepath(object):
    
    INSTANCE = None
    
    def __init__(self):
        #Ver con anibal.
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        self.base_project_path = base_path + "/"
        self.delivery_file_path = base_path + "/workspace/delivery_files/"
        self.practice_file_path = base_path + "/workspace/practice_files/"
        self.script_file_path = base_path + "/workspace/automatic_correction_scripts/"
        self.automatic_correction_tmp_dir = base_path + "/workspace/tmp_dir/"
        self.log_path = base_path + "/workspace/log/"
        self.daemon_path = base_path + "/daemon/"
        self.web_path = base_path + "/web/"
        self.model_path = base_path + "/web/seal/"
    
    def get_base_proyect_path(self):
        return self.base_project_path
    
    def get_delivery_path(self):
        return self.delivery_file_path
    
    def get_practice_path(self):
        return self.practice_file_path
    
    def get_script_path(self):
        return self.script_file_path
    
    def get_automatic_correction_tmp_dir(self):
        return self.automatic_correction_tmp_dir
    
    def get_log_path(self):
        return self.log_path
    
    def get_web_path(self):
        return self.web_path
    
    def get_daemon_path(self):
        return self.daemon_path
    
    def get_model_path(self):
        return self.model_path



def get_instance():
    if not Managepath.INSTANCE:
        Managepath.INSTANCE = Managepath()
    return Managepath.INSTANCE
