from auto_correction.publication.publish_results_visitor import PublishResultsVisitor
from auto_correction.log.logger_manager import LoggerManager
from auto_correction.selection.rest_api_helper import RestApiHelper


class PublishResultsVisitorWeb(PublishResultsVisitor):
    """
    
    This is the visitor in charge of publishing the results to the web.
    
    """
    
    HTTP_MAIL_SERIALIZER = 'http://localhost:8000/automaticcorrectionserializer/'
    
    def __init__(self, auth_user, auth_pass):
        self.log = LoggerManager().get_new_logger("result publication")
        self.rest_api_helper = RestApiHelper(auth_user, auth_pass, PublishResultsVisitorWeb.HTTP_MAIL_SERIALIZER)
    
    def visit(self, visitable):
        self.log.debug("publishing results...")
        visitable.automatic_correction.exit_value = visitable.exit_value
        visitable.automatic_correction.captured_stdout = visitable.captured_stdout
        visitable.automatic_correction.status = 1 + (-2 * visitable.exit_value)
        self.rest_api_helper.save_automatic_correction(visitable.automatic_correction)
        self.log.debug("results published in through the web interface.")
    
