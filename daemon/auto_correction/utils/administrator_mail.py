'''
Created on 08/02/2013

@author: martin
'''

import smtplib
from auto_correction.log.logger_manager import LoggerManager
import requests, json

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

    def request_pending_mails(self):
        self.log.info("Request pending mails list")
        mail_request = requests.get(HTTP_SERIALIZER, auth=(SERIALIZER_AUTH_USER, SERIALIZER_AUTH_PASS))
        if (mail_request.status_code == 200):         
            mail_content = mail_request.content
            mails_list = json.loads(mail_content)['results']
            return(mails_list)

    def prepare_mail(self, mail, recipient, subject):
        body = mail['body']
        body = "" + body + ""
        headers = ["From: " + EMAIL_HOST_USER,"Subject: " + subject,
                   "To: " + recipient,"MIME-Version: 1.0","Content-Type: text/html"]
        headers = "\r\n".join(headers)
        return(headers + "\r\n\r\n" + body)

    def create_session_server_mail(self):
        session = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) 
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        return(session)         

    def delete_mail(self, mail):
        url_to_delete = HTTP_SERIALIZER + str(mail['id'])
        self.log.debug("Sending delete request for mail id %d", mail['id'])
        response = requests.delete(url_to_delete, auth=(SERIALIZER_AUTH_USER, SERIALIZER_AUTH_PASS))
        self.log.info("Delete response: %s", str(response))
       
    def send_mails(self):     
        mails = self.request_pending_mails()
        if (len(mails) == 0):
            self.log.info("There ara not mails to be delivered")
        else:
            for mail in mails:
                recipient = mail['recipient']
                subject = mail['subject']
                mail_prepared = self.prepare_mail(mail, recipient, subject)
                session = self.create_session_server_mail()
                session.sendmail(EMAIL_HOST_USER, recipient, mail_prepared)
                session.quit()
                self.log.info("Mail sent to " + recipient + " subject " + subject)
                self.delete_mail(mail)
                
                