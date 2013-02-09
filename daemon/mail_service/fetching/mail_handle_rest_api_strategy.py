"""

@author: anibal

"""
from mail_service.fetching.mail_fetch_strategy import MailFetchStrategy
from auto_correction.log.logger_manager import LoggerManager
import requests, json
from mail_service.util.mail import Mail
from mail_service.fetching.json_to_mail_translator import JSONToMailTranslator

class MailHandleRESTAPIStrategy(MailFetchStrategy):
    """
    Implementation of the fetching strategy for mails waiting to be sent through the REST API
    """

    HTTP_OK_RESPONSE = 200

    def __init__(self, http_serializer=None, auth_user=None, auth_pass=None):
        """
        Constructor
        """
        logger_manager = LoggerManager()
        self.log = logger_manager.get_new_logger("administrator mail")
        self.http_serializer = http_serializer
        self.auth_user = auth_user
        self.auth_pass = auth_pass
        
        self.json_translator = JSONToMailTranslator()
        self.requests = requests

        
    def get_pending_mails(self):
        self.log.info("Request pending mails list")
        mail_request = self.requests.get(self.http_serializer, auth=(self.auth_user, self.auth_pass))
        if (mail_request.status_code == MailHandleRESTAPIStrategy.HTTP_OK_RESPONSE):         
            mail_content = mail_request.content
            self.json_translator.json = mail_content
            return self.json_translator.get_mails_list()
    
    def request_mail_deletion(self, mail):
        self.log.debug("Sending delete request for mail id %d", mail.id)
        #response = requests.delete(url_to_delete, auth=(SERIALIZER_AUTH_USER, SERIALIZER_AUTH_PASS))
        return self.requests.delete(self.http_serializer + str(mail.id), auth=(self.auth_user, self.auth_pass))
        