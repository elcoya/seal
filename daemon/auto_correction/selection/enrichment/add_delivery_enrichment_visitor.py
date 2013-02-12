"""

@author: anibal

"""
from auto_correction.selection.enrichment.automatic_correction_enrichment_visitor import AutomaticCorrectionEnrichmentVisitor
import json
from auto_correction.log.logger_manager import LoggerManager

class AddScriptEnrichmentVisitor(AutomaticCorrectionEnrichmentVisitor):
    """
    Visitor instance which must add the delivery file information to the automatic correction entity
    """
    
    def __init__(self, rest_api_helper, json_to_delivery_translator):
        self.log = LoggerManager().get_new_logger("add delivery visitor")
        self.rest_api_helper = rest_api_helper
        self.log.debug("Delivery enrichment visitor created.")
    
    def visit(self, automatic_correction):
        self.log.info("Visiting automatic correction to add delivery information.")
        delivery_data = self.rest_api_helper.get_delivery(automatic_correction.delivery)
        self.log.debug("Delivery information got: %s", delivery_data)
        automatic_correction.delivery = json.loads(delivery_data)['results']['file']
        self.log.debug("Delivery information loaded into automatic correction.")
        