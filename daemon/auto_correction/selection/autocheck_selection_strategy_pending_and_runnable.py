from daemon.selection.autocheck_selection_strategy import AutocheckSelectionStrategy
from seal.model.autocheck import Autocheck

class AutocheckSelectionStrategyPendingAndRunnable(AutocheckSelectionStrategy):
    """
    
    Selection strategy to obtain the autochecks which have yet not been checked and 
    it's status is pending (integer value 0)
    
    """
    
    def __init__(self):
        self.object_manager = Autocheck.objects
    
    def get_autochecks(self):
        pending_autochecks = self.object_manager.filter(status=0)
        return self.filter_autochecks(pending_autochecks)
    
    def filter_autochecks(self, autochecks):
        # TODO: remove autochecks for practices with no script associated
        return autochecks
        