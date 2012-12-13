from auto_correction.publication.publish_results_visitor import PublishResultsVisitor


class PublishResultsVisitorWeb(PublishResultsVisitor):
    """
    
    This is the visitor in charge of publishing the results to the web.
    
    """
    
    def visit(self, visitable):
        visitable.automatic_correction.exit_value = visitable.exit_value
        visitable.automatic_correction.captured_stdout = visitable.captured_stdout
        visitable.automatic_correction.status = 1 + (-2 * visitable.exit_value)
        visitable.automatic_correction.save()