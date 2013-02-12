"""

@author: anibal

"""
from auto_correction.selection.enrichment.automatic_correction_enrichment_visitor import AutomaticCorrectionEnrichmentVisitor
import json
from auto_correction.log.logger_manager import LoggerManager

class AddScriptEnrichmentVisitor(AutomaticCorrectionEnrichmentVisitor):
    """
    Visitor instance which must add the script file information to the automatic correction entity
    """
    
    def __init__(self, rest_api_helper, json_to_delivery_translator):
        self.log = LoggerManager().get_new_logger("add script visitor")
        self.rest_api_helper = rest_api_helper
        self.log.debug("Script enrichment visitor created.")
    
    def visit(self, automatic_correction):
        self.log.info("Visiting automatic correction to add script information.")
        delivery_data = self.rest_api_helper.get_delivery(automatic_correction.delivery)
        self.log.debug("Delivery information got: %s", delivery_data)
        practice_pk = json.loads(delivery_data)['results']['practice']
        practice_data = self.rest_api_helper.get_practice(practice_pk)
        self.log.debug("Practice information got: %s", practice_data)
        script_pk = json.loads(practice_data)['results']['script']