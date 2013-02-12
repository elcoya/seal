"""

@author: anibal

"""

class AutomaticCorrectionEnrichmentVisitor:
    """
    
    Head of the enrichment visitor hierarchy. This visitors are supposed to be called upon the
    automatic correction entities of the daemon to get the additional information required to 
    perform the automatic correction. This would be the files involved in the correction: the
    delivery made by the student and the script to be run as correction.
    
    """
    
    
    
    def visit(self, automatic_correction):
        """
        
        Performs the necessary tasks to enrich the automatic correction. Must load new data in
        the automatic correction.
        
        """
        
        yield None
    
