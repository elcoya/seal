from auto_correction.selection.automatic_correction_selection_strategy import AutomaticCorrectionSelectionStrategy
from seal.model.automatic_correction import AutomaticCorrection
from django.db import transaction

class ListFilter():
    """Filters AutomaticCorrections for which there is no script to be run"""
    
    def __init__(self):
        self.automatic_corrections = None
    
    def set_list(self, automatic_corrections):
        self.automatic_corrections = automatic_corrections
        
    def filter(self):
        return [automatic_corrections for automatic_corrections in self.automatic_corrections if automatic_corrections.delivery.practice.get_script()]

class AutomaticCorrectionSelectionStrategyPendingAndRunnable(AutomaticCorrectionSelectionStrategy):
    """
    
    Selection strategy to obtain the automatic_corrections which have yet not been checked and 
    it's status is pending (integer value 0)
    
    """
    
    
    @transaction.commit_manually
    def flush_transaction(self):
        """
        Flush the current transaction so we don't read stale data
    
        Use in long running processes to make sure fresh data is read from
        the database.  This is a problem with MySQL and the default
        transaction mode.  You can fix it by setting
        "transaction-isolation = READ-COMMITTED" in my.cnf or by calling
        this function at the appropriate moment
        """
        transaction.commit()
    
    def __init__(self):
        self.object_manager = AutomaticCorrection.objects
        self.list_filter = ListFilter()
    
    def get_automatic_corrections(self):
        pending_automatic_corrections = self.object_manager.filter(status=0)
        self.list_filter.set_list(automatic_corrections=pending_automatic_corrections)
        self.flush_transaction()
        return self.list_filter.filter()
