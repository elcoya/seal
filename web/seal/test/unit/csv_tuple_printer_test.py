"""
Created on 19/03/2013

@author: anibal
"""
from django.test import TestCase
from seal.utils.csv_tuple_printer import CsvTuplePrinter
from mock import Mock
import shutil
import os

class CsvTuplePrinterTest(TestCase):
    
    
    def testCsvTuplePrinterMustRecieveOneTupleAndPrintItToTheOutputFile(self):
        csv_tuple_printer = CsvTuplePrinter()
        output_file = Mock()
        csv_tuple_printer.output_file = output_file
        a_tuple = ("field1", "field2", 0)
        
        csv_tuple_printer.put(a_tuple)
        
        stringified_tuple = str(a_tuple[0]) + "," + str(a_tuple[1]) + "," + str(a_tuple[2]) + "\n"
        output_file.write.assert_called_with(stringified_tuple)
    
    def testCsvTuplePrinterMustCloseTheOutputFileWhenCommanded(self):
        csv_tuple_printer = CsvTuplePrinter()
        output_file = Mock()
        csv_tuple_printer.output_file = output_file
        
        csv_tuple_printer.close()
        
        output_file.close.assert_called()
    
    def testCsvTuplePrinterMustCreateTheOutputFileWhenCommanded(self):
        file_name = "/tmp/tmp-output-file.csv"
        shutil.rmtree(file_name, ignore_errors=True) # I make shure the file doesn't exists prevously
        csv_tuple_printer = CsvTuplePrinter()
        
        csv_tuple_printer.open(file_name)
        csv_tuple_printer.close()
        
        self.assertTrue(os.path.exists(file_name))
        shutil.rmtree(file_name, ignore_errors=True)
