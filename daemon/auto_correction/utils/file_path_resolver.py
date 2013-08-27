'''
Created on 26/08/2013

@author: anibal
'''
import re

class FilePathResolver():
    """Head of the path resolver strategy hierarchy. Returns the path unchanged"""
    
    def resolve_path(self, filepath):
        return filepath

class SmartFilePathResolver(FilePathResolver):
    """
    
    Regex based path resolver that can be used when the daemon is used within a
    jail. It is used when SMART_PATH_ROUTING_ENABLED is set to True. 
    
    Whipes out the leading section of the path, before the absolute workspace
    path within the filepath resolved.
    
    """
    
    def __init__(self, path_exp):
        self.workspace_pattern = re.compile("%s.+" % path_exp)
    
    def resolve_path(self, filepath):
        return re.search(self.workspace_pattern, filepath).group()

class HardSettingFilePathResolver(FilePathResolver):
    """
    
    Regex based path resolver that can be used when the daemon is used within a
    jail. It is used when SMART_PATH_ROUTING_ENABLED is set to False and 
    ROOT_FILES_PATH is set to a valid path.
    
    Chops the leading section of the filepath, that matches the filepath being
    resolved.
    
    """
    
    def __init__(self, root_path):
        self.root_path_exp = re.compile("%s(.+)" % root_path)
    
    def resolve_path(self, filepath):
        return re.search(self.root_path_exp, filepath).group(1)
