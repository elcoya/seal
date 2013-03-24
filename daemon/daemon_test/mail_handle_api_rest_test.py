"""
Created on 09/02/2013

@author: anibal
"""
import unittest
from unittest.case import TestCase
from mail_service.fetching.mail_handle_rest_api_strategy import MailHandleRESTAPIStrategy
from mock import Mock
from auto_correction.settings import REST_BASE_URL
from auto_correction import settings


class TestMailFetchFromRESTAPI(TestCase):
    
    HTTP_SERIALIZER_URL = REST_BASE_URL + '/mailserializer/'
    
    def testGetMailsMustCallAnHttpRequestUsingGetMethod(self):
        http_serializer=TestMailFetchFromRESTAPI.HTTP_SERIALIZER_URL
        auth_user='user'
        auth_pass='pass'
        
        mail_handle_rest_api_strategy = MailHandleRESTAPIStrategy(http_serializer, auth_user, auth_pass)
        json_translator_mock = Mock()
        mail_handle_rest_api_strategy.json_translator = json_translator_mock
        requests_mock = Mock()
        mail_handle_rest_api_strategy.requests = requests_mock
        mail_request = Mock()
        mail_request.status_code = 204
        requests_mock.get.return_value = mail_request
        
        mail_handle_rest_api_strategy.get_pending_mails()
        
        requests_mock.get.assert_called_once_with(http_serializer, headers={"KEY":settings.DAEMON_KEY})
    
    def testGetMailsMustCallAnHttpRequestAndSendTheResponseToJsonTranslator(self):
        http_serializer=TestMailFetchFromRESTAPI.HTTP_SERIALIZER_URL
        auth_user='user'
        auth_pass='pass'
        
        mail_handle_rest_api_strategy = MailHandleRESTAPIStrategy(http_serializer, auth_user, auth_pass)
        json_translator_mock = Mock()
        mail_handle_rest_api_strategy.json_translator = json_translator_mock
        requests_mock = Mock()
        mail_handle_rest_api_strategy.requests = requests_mock
        mail_request = Mock()
        requests_mock.get.return_value = mail_request
        mail_request.status_code = 200
        mail_request.content = Mock()
        
        mail_handle_rest_api_strategy.get_pending_mails()
        
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