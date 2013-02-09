"""
Created on 09/02/2013

@author: anibal
"""
import unittest
from unittest.case import TestCase
from mail_service.fetching.mail_fetch_from_rest_api_strategy import MailFetchFromRESTAPIStrategy
from mock import Mock


class TestMailFetchFromRESTAPI(TestCase):

    def testName(self):
        http_serializer="http://localhost:8000/mailserializer/"
        auth_user='user'
        auth_pass='pass'
        
        mail_fetch_from_rest_api_strategy = MailFetchFromRESTAPIStrategy(http_serializer, auth_user, auth_pass)
        json_translator_mock = Mock()
        mail_fetch_from_rest_api_strategy.json_translator = json_translator_mock
        requests_mock = Mock()
        mail_fetch_from_rest_api_strategy.requests = requests_mock
        
        mail_fetch_from_rest_api_strategy.get_pending_mails()
        
        requests_mock.get.assert_called_once_with(http_serializer, auth=(auth_user, auth_pass))
        json_translator_mock.get_mails_list.assert_called()
