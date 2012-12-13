from auto_correction.selection.autocheck_selection_strategy import AutocheckSelectionStrategy
from seal.model.autocheck import Autocheck
from django.db import transaction

class ListFilter():
    """Filters Autochecks for which there is no script to be run"""
    
    def __init__(self):
        self.autochecks = None
    
    def set_list(self, autochecks):
        self.autochecks = autochecks
        
    def filter(self):
        return [autocheck for autocheck in self.autochecks if autocheck.delivery.practice.script_set.all()]

class AutocheckSelectionStrategyPendingAndRunnable(AutocheckSelectionStrategy):
    """
    
    Selection strategy to obtain the autochecks which have yet not been checked and 
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
        self.object_manager = Autocheck.objects
        self.list_filter = ListFilter()
    
    def get_autochecks(self):
        self.flush_transaction()
        pending_autochecks = self.object_manager.filter(status=0)
        self.list_filter.set_list(autochecks=pending_autochecks)
        return self.list_filter.filter()
