from auto_correction.publication.publish_results_visitor import PublishResultsVisitor
from auto_correction.log.logger_manager import LoggerManager


class PublishResultsVisitorWeb(PublishResultsVisitor):
    """
    
    This is the visitor in charge of publishing the results to the web.
    
    """
    
    def __init__(self):
        self.log = LoggerManager().get_new_logger("result publication")
    
    def visit(self, visitable):
        self.log.debug("publishing results...")
        visitable.automatic_correction.exit_value = visitable.exit_value
        visitable.automatic_correction.captured_stdout = visitable.captured_stdout
        visitable.automatic_correction.status = 1 + (-2 * visitable.exit_value)
        visitable.automatic_correction.save()
        self.log.debug("results published.")