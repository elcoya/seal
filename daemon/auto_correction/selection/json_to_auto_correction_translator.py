"""

@author: anibal

"""
from auto_correction.log.logger_manager import LoggerManager
import json
from auto_correction.utils.automatic_correction import AutomaticCorrection
from auto_correction.utils.managepath import Managepath
from auto_correction.utils import managepath

class JSONToAutoCorrectionTranslator():
    """
    This class' responsability is limited to generate automatic correction entities out of the json strings recieved from the rest api
    """


    def __init__(self, input_str=None):
        """
        Initializes the json string that should be turn into a local entity
        """
        self.log = LoggerManager().get_new_logger("auto correction-json translator")
        self.json = input_str
        self.filepath_resolver = managepath.get_instance().get_filepath_resolver()
    
    def get_automatic_corrections(self):
        self.log.debug("parsing: %s", self.json)
        automatic_correction_data_list = json.loads(self.json)['results']
        automatic_correction_list = []
        for automatic_correction_data in automatic_correction_data_list:
            automatic_correction = AutomaticCorrection(automatic_correction_data['id'])
            automatic_correction.captured_stdout = automatic_correction_data['captured_stdout']
            automatic_correction.exit_value = automatic_correction_data['exit_value']
            automatic_correction.status = automatic_correction_data['status']
            automatic_correction.delivery_id = automatic_correction_data['delivery']
            
            automatic_correction.delivery = self.filepath_resolver.resolve_path(automatic_correction_data['get_delivery_file'])
            automatic_correction.script = self.filepath_resolver.resolve_path(automatic_correction_data['get_correction_script'])

            automatic_correction.user_mail = automatic_correction_data['user_mail']
            automatic_correction_list.append(automatic_correction);
        return automatic_correction_list

    def resolve_file_path(self, filepath):
        if(Managepath.is_smart_file_routing_enabled()):
            
        else if ():
            
        else:
            
    
    
    