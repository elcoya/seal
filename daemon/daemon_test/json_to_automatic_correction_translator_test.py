"""
@author: anibal
"""
import unittest
from mail_service.fetching.json_to_mail_translator import JSONToMailTranslator
from auto_correction.selection.json_to_auto_correction_translator import JSONToAutoCorrectionTranslator


class TestJSONToAutomaticCorrectionTranslator(unittest.TestCase):


    def testJSONToAutomaticTranstalorMustTakeJSONStringContainingInformationAndReturnAListOfAutomaticCorrectionEntities(self):

        jsonstring = '{"count": 1, "next": null, "previous": null, "results": [{"id": 1, "delivery": 1,\
                       "captured_stdout": "Successful run!", "exit_value": 0, "status": 1,\
                       "get_delivery_file": "/tmp/delivery.zip", "get_correction_script": "/tmp/script.sh",\
                       "user_mail": "sealstudent@gmail.com"}]}'
        translator = JSONToAutoCorrectionTranslator(input_str=jsonstring)
        
        atomatic_corrections = translator.get_automatic_corrections()
        
        atomatic_correction = atomatic_corrections[0]
        self.assertEqual(atomatic_correction.pk, 1)
        self.assertEqual(atomatic_correction.delivery_id, 1)
        self.assertEqual(atomatic_correction.captured_stdout, "Successful run!")
        self.assertEqual(atomatic_correction.exit_value, 0)
        self.assertEqual(atomatic_correction.delivery, "/tmp/delivery.zip")
        self.assertEqual(atomatic_correction.script, "/tmp/script.sh")
        self.assertEqual(atomatic_correction.user_mail, "sealstudent@gmail.com")
