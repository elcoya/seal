'''
Created on 30/01/2013

@author: martin
'''
import os
from auto_correction import settings

class Managepath(object):
    
    INSTANCE = None
    
    def __init__(self):
        
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))        
        self.base_project_path = base_path + "/"
        self.daemon_path = base_path + "/daemon/"
        
        self.workspace_file_path = settings.WORKSPACE_PATH
        self.automatic_correction_tmp_dir = settings.AUTOMATIC_CORRECTION_TMP_PATH
        self.log_path = settings.LOG_PATH
            
    def get_base_proyect_path(self):
        return self.base_project_path
    
    def get_workspace_proyect_path(self):
        return self.workspace_file_path
    
    def get_automatic_correction_tmp_dir(self):
        return self.automatic_correction_tmp_dir
    
    def get_log_path(self):
        return self.log_path
    
    def get_daemon_path(self):
        return self.daemon_path

def get_instance():
    if not Managepath.INSTANCE:
        Managepath.INSTANCE = Managepath()
    return Managepath.INSTANCE
