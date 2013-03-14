"""
Created on 09/02/2013

@author: anibal
"""
import unittest
from unittest.case import TestCase
from mail_service.fetching.mail_handle_rest_api_strategy import MailHandleRESTAPIStrategy
from mock import Mock


class TestMailFetchFromRESTAPI(TestCase):
    
    HTTP_SERIALIZER_URL = "http://localhost:8000/mailserializer/"
    
    def testGetMailsMustCallAnHttpRequestUsingGetMethod(self):
        http_serializer=TestMailFetchFromRESTAPI.HTTP_SERIALIZER_URL
        auth_user='user'
        auth_pass='pass'
        
        mail_handle_rest_api_strategy = MailHandleRESTAPIStrategy(http_serializer, auth_user, auth_pass)
        json_translator_mock = Mock()
        mail_handle_rest_api_strategy.json_translator = json_translator_mock
        requests_mock = Mock()
        mail_handle_rest_api_strategy.requests = requests_mock
        
        mail_handle_rest_api_strategy.get_pending_mails()
        
        requests_mock.get.assert_called_once_with(http_serializer, auth=(auth_user, auth_pass))
        json_translator_mock.get_mails_list.assert_called()

    def testDeleteMailsMustCallAnHttpRequestUsingDeleteMethod(self):
        http_serializer=TestMailFetchFromRESTAPI.HTTP_SERIALIZER_URL
        auth_user='user'
        auth_pass='pass'
        
        mail_handle_rest_api_strategy = MailHandleRESTAPIStrategy(http_serializer, auth_user, auth_pass)
        requests_mock = Mock()
        mail_handle_rest_api_strategy.requests = requests_mock
        mail = Mock()
        mail.id = 1
        
        mail_handle_rest_api_strategy.request_mail_deletion(mail)
        
        requests_mock.delete.assert_called()