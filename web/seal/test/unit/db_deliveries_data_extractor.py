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
        
        practices = Mock()
        practice_mock = Mock()
        practices.all.return_value = [practice_mock,]
        
        students = Mock()
        student_all_return_value = Mock()
        student_mock = Mock()
        student_all_return_value.order_by.return_value = [student_mock,]
        students.all.return_value = student_all_return_value
        
        db_deliveries_extractor = DbDeliveriesExtractor()
        db_deliveries_extractor.objects = objects
        db_deliveries_extractor.students = students
        db_deliveries_extractor.practices = practices
        
        db_deliveries_extractor.get_data()
        
        objects.filter.assert_called()
    
    def testDataExtractorMustReturnAListContainingTheDataToBeExported(self):
        objects = Mock()
        delivery_mock = Mock()
        delivery_mock.practice.uid = "1"
        filter_return_value = Mock()
        filter_return_value.status = 1
        objects.filter.return_value = filter_return_value
        delivery_mock.get_automatic_correction.return_value = filter_return_value
        filter_return_value.order_by.return_value = [delivery_mock,]
        
        practices = Mock()
        practice_mock = Mock()
        practice_mock.uid = "2"
        practices.all.return_value = [practice_mock,]
        
        students = Mock()
        student_all_return_value = Mock()
        student_mock = Mock()
        student_all_return_value.order_by.return_value = [student_mock,]
        students.all.return_value = student_all_return_value
        
        db_deliveries_extractor = DbDeliveriesExtractor()
        db_deliveries_extractor.objects = objects
        db_deliveries_extractor.students = students
        db_deliveries_extractor.practices = practices
        
        
        result_value = db_deliveries_extractor.get_data()
        
        first_expected = (delivery_mock.practice.uid, delivery_mock.student.uid, delivery_mock.student.user.first_name, delivery_mock.student.user.last_name, 
                          "aprobado", delivery_mock.get_correction.return_value.grade)
        second_expected = (practice_mock.uid, student_mock.uid, student_mock.user.first_name, student_mock.user.last_name, 
                          "pendiente", None)
        expected_value = [first_expected, second_expected,]
        self.assertEquals(result_value, expected_value)
