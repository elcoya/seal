"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from seal.model import Practice, Course
from seal.model.script import Script
from seal.test.integration.utils import clean_up_database_tables,\
    create_a_course, create_a_student, create_a_practice, load_a_script,\
    create_a_delivery, create_an_automatic_correction, create_a_shift

class PracticeIntegrationTest(TestCase):
    
    student = None
    practice = None
    course = None
    script = None
    delivery = None
    automatic_correction = None

    course_name = "2012-2"
    shift_name = "miercoles"
    student_name = "student"
    student_email = "student@foo.foo"
    practice_deadline = '2012-12-31'
    practice_filepath = "practice_filepath"
    practice_uid = "practice_uid"
    script_file = "/home/anibal/workspace/python-aptana-wkspace/seal/daemon/feature_test/data/successfull_test_script.sh"
    delivery_filepath = "/home/anibal/workspace/python-aptana-wkspace/seal/daemon/feature_test/data/delivery.zip"
    delivery_date = '2012-12-15'
    stdout = "some generated stdout"
    exit_value = 0
    status = 1

    
    def setUp(self):
        nameCourse = '2012-2'
        self.course = Course()
        self.course.name = nameCourse
        self.course.save()
    
    def tearDown(self):
        Practice.objects.filter(uid="1").delete()
        pCourse = Course.objects.get(name='2012-2')
        pCourse.delete()
      
    def testPracticeCreationCompareName(self):
        pPractice = Practice()
        pPractice.uid = "1"
        pPractice.course = self.course
        pPractice.file = "pathFile"
        pPractice.deadline = "2012-12-01" 
        pPractice.save()
        cPractice = Practice.objects.get(uid="1")
        self.assertEqual(pPractice.course.name, cPractice.course.name)
    
    def testPracticeShouldFeatureSomeWrapperToAccessTheAssociatedScript(self):
        practice = Practice()
        practice.uid = "uid"
        practice.course = self.course
        practice.file = "pathFile"
        practice.deadline = "2012-12-01" 
        practice.save()
        script = Script()
        script.practice = practice
        script.save()
        self.assertEquals(practice.get_script(), script)

    def testGetDistinctSuccessfullDeliveriesCount(self):
        clean_up_database_tables()
        self.course = create_a_course(self.course_name)
        self.shift = create_a_shift(self.shift_name, self.course_name)
        self.student = create_a_student(self.student_name, self.shift_name)
        self.practice = create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        self.delivery1 = create_a_delivery(self.delivery_filepath, self.student_name, self.course_name, self.practice_uid, self.delivery_date)
        self.automatic_correction1 = create_an_automatic_correction(self.delivery_filepath, self.stdout, self.exit_value, self.status)
        
        self.assertEquals(1, self.practice.get_successfull_deliveries_count())
    
    def testGetDistinctFailedDeliveriesCount(self):
        clean_up_database_tables()
        self.course = create_a_course(self.course_name)
        self.shift = create_a_shift(self.shift_name, self.course_name)
        self.student = create_a_student(self.student_name, self.shift_name)
        self.practice = create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        self.delivery1 = create_a_delivery(self.delivery_filepath, self.student_name, self.course_name, self.practice_uid, self.delivery_date)
        self.automatic_correction1 = create_an_automatic_correction(self.delivery_filepath, self.stdout, self.exit_value, self.status)
        
        self.assertEquals(0, self.practice.get_failed_deliveries_count())
    
    def testGetDistinctPendingDeliveriesCount(self):
        clean_up_database_tables()
        self.course = create_a_course(self.course_name)
        self.shift = create_a_shift(self.shift_name, self.course_name)
        self.student = create_a_student(self.student_name, self.shift_name)
        self.practice = create_a_practice(self.course_name, self.practice_deadline, self.practice_filepath, self.practice_uid)
        
        self.assertEquals(1, self.practice.get_students_pending_deliveries_count())
    
