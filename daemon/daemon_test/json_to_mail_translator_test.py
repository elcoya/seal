"""
@author: anibal
"""
import unittest
from mail_service.fetching.json_to_mail_translator import JSONToMailTranslator


class TestJSONToMailTranslator(unittest.TestCase):


    def testJSONToMailTranstalorMustTakeJSONStringContainingInformationAndReturnAListOfMailEntities(self):
        jsonstring = '{"count": 1, "next": null, "previous": null, "results": [{"id": 10, "subject": "Registration SEAL Successful", "body": "You have been registered in SEAL with username: martinmaurozucchiatti and password: 1234", "recipient": "tanomartin05@gmail.com"}]}'
        translator = JSONToMailTranslator(json_str=jsonstring)
        
        mails = translator.get_mails_list()
        
        mail = mails[0]
        self.assertEqual(mail.id, 10)
        self.assertEqual(mail.subject, "Registration SEAL Successful")
        self.assertEqual(mail.recipient, "tanomartin05@gmail.com")
        self.assertEqual(mail.body, "You have been registered in SEAL with username: martinmaurozucchiatti and password: 1234")
