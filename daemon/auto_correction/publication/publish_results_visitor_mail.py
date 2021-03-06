"""

@author: anibal

"""
from auto_correction.publication.publish_results_visitor import PublishResultsVisitor
from auto_correction.log.logger_manager import LoggerManager
from auto_correction.selection.rest_api_helper import RestApiHelper
from mail_service.util.mail import Mail
from django.utils.encoding import smart_str
from auto_correction.settings import REST_BASE_URL

class PublishResultsVisitorMail(PublishResultsVisitor):
    """
    Implementation of the publishing visitor which posts a mail through the web interface to await sending
    """
    
    HTTP_MAIL_SERIALIZER = REST_BASE_URL + '/mailserializer/'
    STATUS_STRINGS = {-1:"failed", 0:"pending", 1:"successfull"}
    STATUS_UNKNOWN = 'unknown status'
    
    def __init__(self, auth_user, auth_pass):
        self.log = LoggerManager().get_new_logger("result publication mail")
        self.rest_api_helper = RestApiHelper(auth_user, auth_pass, 
                                             http_mail_serializer=PublishResultsVisitorMail.HTTP_MAIL_SERIALIZER)
    
    def get_status(self, status=10):
        """Returns a status raw value as a human readable value"""
        self.log.debug("translating status %d", status)
        try:
            status_string = PublishResultsVisitorMail.STATUS_STRINGS[status]
        except:
            status_string = PublishResultsVisitorMail.STATUS_UNKNOWN
        return status_string
    
    def build_mail(self, result):
        self.log.debug("building mail...")
        mail = Mail()
        mail.subject = "Resultado de la correccion automatica"
        mail.recipient = result.automatic_correction.user_mail
        exit_value = result.exit_value
        mail.body = "Ejecucion "
        if(exit_value==0):
            mail.body += "exitosa, trabajo aprobado"
        else:
            mail.body += "fallida, trabajo no aprobado. Puede corregirlo y volver a intentarlo"
        mail.body += ".\n\n"
        return mail
    
    def visit(self, visitable):
        self.log.debug("publishing results...")
        visitable.automatic_correction.exit_value = visitable.exit_value
        visitable.automatic_correction.captured_stdout = visitable.captured_stdout
        visitable.automatic_correction.status = 1 + (-2 * visitable.exit_value)
        mail = self.build_mail(visitable)
        self.rest_api_helper.save_mail(mail)
        self.log.debug("results published in through mail.")
    
