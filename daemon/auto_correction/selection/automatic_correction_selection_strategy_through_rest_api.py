"""

@author: anibal

"""
from auto_correction.selection.automatic_correction_selection_strategy import AutomaticCorrectionSelectionStrategy
from auto_correction.log.logger_manager import LoggerManager
from auto_correction.selection.rest_api_helper import RestApiHelper

class AutomaticCorrectionSelectionStrategyThroughRestApi(AutomaticCorrectionSelectionStrategy):
    """
    Implementation of the selection strategy that brings the automatic correction information from the rest api
    """
    
    HTTP_AUTOMATIC_CORRECTION_SERIALIZER = 'http://localhost:8000/richautomaticcorrectionserializer/'
    
    def __init__(self, auth_user, auth_pass):
        """
        Constructor
        """
        self.log = LoggerManager().get_new_logger("auto correction selection")
        self.rest_api_helper = RestApiHelper(auth_user, auth_pass, 
                                             AutomaticCorrectionSelectionStrategyThroughRestApi.HTTP_AUTOMATIC_CORRECTION_SERIALIZER)
    
    def get_automatic_corrections(self):
        self.log.debug("searching for deliveries with status pending...")
        pending_automatic_corrections = self.rest_api_helper.get_automatic_corrections()
        count = len(pending_automatic_corrections)
        if count > 0:
            self.log.debug("%d deliveries obtained.", count)
        return pending_automatic_corrections


