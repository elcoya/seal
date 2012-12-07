from daemon.publication.publish_results_visitor import PublishResultsVisitor


class PublishResultsVisitorWeb(PublishResultsVisitor):
    """
    
    This is the visitor in charge of publishing the results to the web.
    
    """
    
    def visit(self, visitable):
        visitable.autocheck.exit_value = visitable.exit_value
        visitable.autocheck.captured_stdout = visitable.captured_stdout
        visitable.autocheck.status = 1 + (-2 * visitable.exit_value)
        visitable.autocheck.save()