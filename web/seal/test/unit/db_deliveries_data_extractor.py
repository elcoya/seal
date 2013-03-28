"""
Created on 19/03/2013

@author: anibal
"""
from django.test import TestCase
from mock import Mock
from seal.util.db_deliveries_data_extractor import DbDeliveriesExtractor

class DbDeliveriesDataExtractorUnitTest(TestCase):
    
    def testDataExtractorInvokeFilterMethodFromTheORM(self):
        objects = Mock()
        delivery_mock = Mock()
        filter_return_value = Mock()
        filter_return_value.status = 1
        objects.filter.return_value = filter_return_value
        delivery_mock.get_automatic_correction.return_value = filter_return_value
        filter_return_value.order_by.return_value = [delivery_mock,]
        db_deliveries_extractor = DbDeliveriesExtractor()
        db_deliveries_extractor.objects = objects
        
        db_deliveries_extractor.get_data()
        
        objects.filter.assert_called()
    
    def testDataExtractorMustReturnAListContainingTheDataToBeExported(self):
        objects = Mock()
        delivery_mock = Mock()
        filter_return_value = Mock()
        filter_return_value.status = 1
        objects.filter.return_value = filter_return_value
        delivery_mock.get_automatic_correction.return_value = filter_return_value
        filter_return_value.order_by.return_value = [delivery_mock,]
        db_deliveries_extractor = DbDeliveriesExtractor()
        db_deliveries_extractor.objects = objects
        
        result_value = db_deliveries_extractor.get_data()
        
        unique_expected = (delivery_mock.practice.uid, delivery_mock.student.uid, delivery_mock.student.user.first_name, delivery_mock.student.user.last_name, 
                          "aprobado", delivery_mock.get_correction.return_value.grade)
        expected_value = [unique_expected, ]
        self.assertEquals(result_value, expected_value)
