"""
@author: anibal
"""
from unittest.case import TestCase
from mail_service.util.mail import Mail


class TestMailUtilityClass(TestCase):
    
    id = 1
    recipient = 'username@recipients.domain'
    subject = 'test subject'
    body = 'E-Mail body for this test'
    email_host_user = 'email host user'
    
    expected_result = \
        "From: " + email_host_user + "\r\n" + \
        "Subject: " + subject + "\r\n" + \
        "To: " + recipient + "\r\n" + \
        "MIME-Version: 1.0" + "\r\n" + \
        "Content-Type: text/html" + "\r\n\r\n" + \
        body
    
    def testMailBuildToSendMethodMustReturnTheStringThatCanBeSentByTheMailService(self):
        mail = Mail()
        mail.id = self.id
        mail.recipient = self.recipient
        mail.subject = self.subject
        mail.body = self.body
        
        sendable_string = mail.build_to_send_from_host(self.email_host_user)
        
        self.assertEquals(self.expected_result, sendable_string)
