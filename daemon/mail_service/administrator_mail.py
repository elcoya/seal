"""
Created on 08/02/2013

@author: martin
"""

import smtplib
from auto_correction.log.logger_manager import LoggerManager
import requests, json
from mail_service.fetching.mail_handle_rest_api_strategy import MailHandleRESTAPIStrategy
from mail_service.preparation.mail_session_helper import MailSessionHelper

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sealteacher@gmail.com'
EMAIL_HOST_PASSWORD = 'sealtpprof'
EMAIL_PORT = 587

HTTP_SERIALIZER = 'http://localhost:8000/mailserializer/'
SERIALIZER_AUTH_USER = 'seal'
SERIALIZER_AUTH_PASS = 'seal'

class AdministratorMail(object):

    def __init__(self):
        logger_manager = LoggerManager()
        self.log = logger_manager.get_new_logger("administrator mail")
        self.mail_handle_strategy = MailHandleRESTAPIStrategy(
                                                          http_serializer=HTTP_SERIALIZER, 
                                                          auth_user=SERIALIZER_AUTH_USER, 
                                                          auth_pass=SERIALIZER_AUTH_PASS)
        self.session_helper = MailSessionHelper(email_host=EMAIL_HOST, 
                                                         email_port=EMAIL_PORT, 
                                                         email_host_user=EMAIL_HOST_USER, 
                                                         email_host_password=EMAIL_HOST_PASSWORD)
        
    def send_mails(self):
        mails = self.mail_handle_strategy.get_pending_mails()
        if (len(mails)==0):
            self.log.info("There ara not mails to be delivered")
        else:
            self.log.info("Found %d mails awaiting sending.", len(mails))
            session = self.session_helper.get_server_session()
            for mail in mails:
                session.sendmail(EMAIL_HOST_USER, mail.recipient, mail.build_to_send_from_host(EMAIL_HOST_USER))
                self.log.info("Mail sent to %s (subject: %s)", mail.recipient, mail.subject)
                response = self.mail_handle_strategy.request_mail_deletion(mail)
                self.log.info("Delete response: %s", str(response))
            self.session_helper.close_server_session(session)

