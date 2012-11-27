import unittest
from seal.model.autocheck import Autocheck

class TestAutocheckRunner(unittest.TestCase):


    def setUp(self):
        autocheck = Autocheck.objects.all().delete


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()