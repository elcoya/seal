'''
Created on 30/01/2013

@author: martin
'''
import os

class Managepath(object):
    
    def __init__(self):
        #Ver con anibal.
        BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        self.BASE_PROJECT_PATH = BASE_PATH + "/"
        self.DELIVERY_FILE_PATH = BASE_PATH + "/workspace/delivery_files/"
        self.PRACTICE_FILE_PATH = BASE_PATH + "/workspace/practice_files/"
        self.SCRIPT_FILE_PATH = BASE_PATH + "/workspace/automatic_correction_scripts/"
        self.DAEMON_PATH = BASE_PATH + "/daemon/"
        self.WEB_PATH = BASE_PATH + "/web/"
        self.BEHAVE_PATH = BASE_PATH + "/web/seal/"
    
    def get_base_proyect_path(self):
        return self.BASE_PROJECT_PATH
    
    def get_delivery_path(self):
        return self.DELIVERY_FILE_PATH
    
    def get_practice_path(self):
        return self.PRACTICE_FILE_PATH
    
    def get_script_path(self):
        return self.SCRIPT_FILE_PATH
    
    def get_web_path(self):
        return self.WEB_PATH
    
    def get_daemon_path(self):
        return self.DAEMON_PATH
    
    def get_behave_path(self):
        return self.BEHAVE_PATH