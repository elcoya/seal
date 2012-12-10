
class PublishResultsVisitor:
    """
    
    Head of the visitor hierarchy. The visitors are in charge of publishing the
    results of the scripts run for the deliveries made.
    
    """
    
    def visit(self, visitable):
        yield None
