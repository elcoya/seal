"""
@author: anibal
"""
import unittest
from mail_service.administrator_mail import AdministratorMail
from mock import Mock


class TestMailAdministrator(unittest.TestCase):


    def testSendMailsMustIterateTheMailsToBeSentAndPassThemToTheServerSessionObtainedFromTheServerHandler(self):
        mail_administrator = AdministratorMail()
        session_helper_mock = Mock()
        session_mock = Mock()
        session_helper_mock.get_server_session.return_value = session_mock
        mail_fetch_strategy_mock = Mock()
        pending_mails = (Mock(), Mock(), Mock())
        mail_fetch_strategy_mock.get_pending_mails.return_value = pending_mails
        mail_administrator.mail_handle_strategy = mail_fetch_strategy_mock
        mail_administrator.session_helper = session_helper_mock
        
        mail_administrator.send_mails()
        
        session_helper_mock.get_server_session.assert_called()
        session_helper_mock.close_server_session.assert_called()
        session_mock.sendmail.assert_called()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSendMailsMustIterateTheMailsToBeSentAndPassThemToTheServerSessionObtainedFromTheServerHandler']
    unittest.main()