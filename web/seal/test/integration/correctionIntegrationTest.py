from django.test import TestCase
from seal.model.correction import Correction
from seal.model.delivery import Delivery
from seal.model.practice import Practice
from seal.model.course import Course
from seal.model.student import Student
from seal.model.suscription import Suscription
from django.contrib.auth.models import User
from seal.model.teacher import Teacher
from seal.model.shift import Shift

class CorrectionIntegrationTest(TestCase):
    
    course_name = "course_name"
    shift_name = "tarde"
    student_name = "student"
    teacher_name = "teacher"
    teacher_appointment = "teacher"
    student_email = "email@student.foo"
    teacher_email = "teacher@teacher.foo"
    practice_deadline = "2012-12-01"
    practice_filepath = "filepath"
    practice_uid = "practice_uid"
    delivery_filepath = "delivery_filepath"
    delivery_date = "2012-11-30"
    correction_public_comment = "Public Comment for test"
    correction_private_comment = "Private Comment for test"
    correction_grade = 4.0
    
    def create_a_course(self):
        course = Course()
        course.name = self.course_name
        course.save()
    
    def create_a_practice(self):
        practice = Practice()
        practice.course = Course.objects.get(name=self.course_name)
        practice.deadline = self.practice_deadline
        practice.file = self.practice_filepath
        practice.uid = self.practice_uid
        practice.save()
    
    def get_user_for_student(self):
        user = User.objects.get_or_create(username=self.student_name)[0]
        user.set_password(self.student_name)
        user.save()
        return user
    
    def create_a_student(self):
        student = Student()
        student.uid = self.student_name
        student.user = self.get_user_for_student()
        student.save() 
        student.shifts.add(Shift.objects.get(name=self.shift_name))
        student.save()
    
    def create_a_shift(self):
        shift = Shift()
        shift.name = self.shift_name
        shift.description = self.shift_name
        shift.course = Course.objects.get(name=self.course_name)
        shift.save()
        return shift

    
    def create_a_teacher(self):
        teacher = Teacher()
        teacher.uid = self.teacher_name
        teacher.user = self.get_user_for_student()
        teacher.appointment = self.teacher_appointment
        teacher.save()
    
    def create_a_delivery(self):
        delivery = Delivery()
        delivery.file = self.delivery_filepath
        delivery.student = Student.objects.get(uid=self.student_name)
        course = Course.objects.get(name=self.course_name)
        delivery.practice = Practice.objects.get(course=course, uid=self.practice_uid)
        delivery.deliverDate = self.delivery_date
        delivery.save()
    
    def setUp(self):
        Correction.objects.all().delete()
        Delivery.objects.all().delete()
        Practice.objects.all().delete()
        Suscription.objects.all().delete()
        Course.objects.all().delete()
        Student.objects.all().delete()
        Teacher.objects.all().delete()
        
        self.create_a_course()
        self.create_a_shift()
        self.create_a_practice()
        self.create_a_student()
        self.create_a_delivery()
        self.create_a_teacher()
        
        
    def test_correction_creation(self):
        correction = Correction()
        correction.publicComent = self.correction_public_comment
        correction.privateComent = self.correction_private_comment
        correction.grade = self.correction_grade
        delivery = Delivery.objects.get(file=self.delivery_filepath)
        teacher = Teacher.objects.get(uid=self.teacher_name)
        correction.delivery = delivery
        correction.corrector = teacher
        correction.save()
        
        corrections = Correction.objects.all()
        self.assertEqual(len(corrections), 1) # as I have deleted them all, there can be only 1
        self.assertEqual(corrections[0], correction)
        saved_correction = corrections[0]
        self.assertEqual(saved_correction.publicComent, self.correction_public_comment)
        self.assertEqual(saved_correction.privateComent, self.correction_private_comment)
        self.assertEqual(saved_correction.grade, self.correction_grade)
