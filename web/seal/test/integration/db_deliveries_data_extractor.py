"""
Created on 19/03/2013

@author: anibal
"""
from django.test import TestCase
from mock import Mock
from seal.util.db_deliveries_data_extractor import DbDeliveriesExtractor
from seal.model.delivery import Delivery
from seal.test.integration import utils
from django.contrib.auth.models import User
from seal.model.correction import Correction

class DbDeliveriesDataExtractorIntegrationTest(TestCase):
    
    teacher_name = u"teacher"
    teacher_first_name = u"Test"
    teacher_last_name = u"Teacher"
    
    course_name = "course"
    shift_name = "shift"
    student_name_1 = u"student A"
    student_name_2 = u"student B"
    
    student_first_name_1 = u"Name1"
    student_last_name_1 = u"Surname1"
    student_first_name_2 = u"Name2"
    student_last_name_2 = u"Surname2"
    
    practice_deadline = "2013-04-15"
    practice_filepath = "/tmp/does_not_matter.ext"
    practice_uid = u"practice"
    
    delivery_date1 = "2013-04-12"
    delivery_date2 = "2013-04-13"
    delivery_filepath1 = "/tmp/does_not_matter_either_1.ext"
    delivery_filepath2 = "/tmp/does_not_matter_either_2.ext"
    delivery_filepath3 = "/tmp/does_not_matter_either_3.ext"
    delivery_filepath4 = "/tmp/does_not_matter_either_4.ext"
    
    automatic_result_successfull = "aprobado"
    automatic_result_failed = "desaprobado"
    
    def setUp(self):
        utils.clean_up_database_tables()
        
        teacher = utils.create_a_teacher(self.teacher_name)
        teacher.user.first_name = self.teacher_first_name
        teacher.user.last_name = self.teacher_last_name
        teacher.user.save()
        
        self.course = utils.create_a_course(self.course_name)
        shift = utils.create_a_shift(self.shift_name, self.course_name)
        practice = utils.create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        
        student1 = utils.create_a_student(self.student_name_1, self.shift_name)
        student1.user.first_name = self.student_first_name_1
        student1.user.last_name = self.student_last_name_1
        student1.user.save()
        
        student2 = utils.create_a_student(self.student_name_2, self.shift_name)
        student2.user.first_name = self.student_first_name_2
        student2.user.last_name = self.student_last_name_2
        student2.user.save()
        
        delivery_1_student_1 = utils.create_a_delivery(self.delivery_filepath1, self.student_name_1, self.course_name, self.practice_uid, self.delivery_date1)
        delivery_2_student_1 = utils.create_a_delivery(self.delivery_filepath2, self.student_name_1, self.course_name, self.practice_uid, self.delivery_date2)
        
        delivery_1_student_2 = utils.create_a_delivery(self.delivery_filepath3, self.student_name_2, self.course_name, self.practice_uid, self.delivery_date1)
        delivery_2_student_2 = utils.create_a_delivery(self.delivery_filepath4, self.student_name_2, self.course_name, self.practice_uid, self.delivery_date1)
        
        automatic_correction_1_1 = utils.create_an_automatic_correction(self.delivery_filepath1, "test automatic stdout", 1, -1)
        automatic_correction_2_1 = utils.create_an_automatic_correction(self.delivery_filepath2, "test automatic stdout", 0, 1)
        
        automatic_correction_1_2 = utils.create_an_automatic_correction(self.delivery_filepath3, "test automatic stdout", 1, -1)
        automatic_correction_2_2 = utils.create_an_automatic_correction(self.delivery_filepath4, "test automatic stdout", 0, 0)
        
        manual_correction = Correction()
        manual_correction.delivery = delivery_2_student_1
        manual_correction.grade = 8
        manual_correction.corrector = teacher
        manual_correction.save()
    
    
    def testDataExtractorMustReturnAListOfTuplesContainingTheDataToBeExported(self):
        db_deliveries_extractor = DbDeliveriesExtractor()
        db_deliveries_extractor.course = self.course
        
        result_list = db_deliveries_extractor.get_data()
        
        first_entry = (self.practice_uid, self.student_name_1, self.student_first_name_1, self.student_last_name_1, self.automatic_result_successfull, 8)
        second_entry = (self.practice_uid,self.student_name_2 , self.student_first_name_2, self.student_last_name_2, self.automatic_result_failed,None)
        
        self.assertEquals(result_list[0], first_entry)
        self.assertEquals(result_list[1], second_entry)
    
