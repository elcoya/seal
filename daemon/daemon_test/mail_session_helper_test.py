"""
@author: anibal
"""
import unittest
from mail_service.preparation.mail_session_helper import MailSessionHelper
from mock import Mock


class TestMailSessionHelper(unittest.TestCase):


    def testMailSendPreparationMustSetUpAProperlyConfiguredSession(self):
        mail_send_preparation = MailSessionHelper()
        smtplib_mock = Mock()
        return_value = Mock()
        smtplib_mock.SMTP.return_value = return_value
        mail_send_preparation.smtplib = smtplib_mock
        
        result = mail_send_preparation.get_server_session()
        
        smtplib_mock.SMTP.assert_called()
        return_value.ehlo.assert_called()
        return_value.starttls.assert_called()
        return_value.ehlo.assert_called()
        return_value.login.assert_called()
        self.assertEqual(result, return_value)
        
        
    def testCloseServerSessionMustInvokeTheSessionQuitMethod(self):
        mail_send_preparation = MailSessionHelper()
        session = Mock()
        
        mail_send_preparation.close_server_session(session)
        
        session.quit.assert_called()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMailSendPreparationMustSetUpAProperlyConfiguredSession']
    unittest.main()