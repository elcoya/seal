from django.test import TestCase
from seal.model.correction import Correction

class CorrectionTest(TestCase):
    
    correction_public_comment = "Public Comment for test"
    correction_private_comment = "Private Comment for test"
    correction_grade = 4.0
    string_compare = "Grade: 4.0 - Public Comment: Public Comment for test"
    
    def testCorrectionToStringReturnGradeAndPublicComment(self):
        correction = Correction()
        correction.publicComent = self.correction_public_comment
        correction.privateComent = self.correction_private_comment
        correction.grade = self.correction_grade
        self.assertEqual(str(correction), self.string_compare)
