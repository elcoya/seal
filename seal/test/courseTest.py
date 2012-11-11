from django.test import TestCase
from seal.model.course import Course
from seal.model.student import Student
from seal.model.practice import Practice
from django.db.utils import IntegrityError

class CourseTest(TestCase):
    def testCourseCreation(self):
        """
        We create a Course with a name and checks it's value.
        """
        aName = '2012-2C'
        aCourse = Course()
        aCourse.name = aName
        self.assertEqual(aCourse.name, aName)
    
    
    def testCourseUniqueName(self):
        """
        I will try to create a Course with the same name as another and expect a failure
        """
        aName = '2012-2C'
        aCourse = Course.objects.get_or_create(name=aName)
        anotherCourse = Course(name=aName)
        self.assertRaises(IntegrityError, anotherCourse.save())
        self.fail('should have rise duplication exception')
    
    def testCourseAddStudent(self):
        """
        I will take a course and add a student to it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')
        aStudent = Student.objects.get_or_create(name="Juan Perez", uid='1234', email = "email@pagnia.com.ar")
        aCourse.student_set.add(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertTrue(aCourse.student_set.contains(aStudent), 'Set, expected to contain Juan Perez')
    
    def testCourseDeleteStudent(self):
        """
        I Will add a Student from a Course and verify it contains the student
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')
        aStudent = Student.objects.get_or_create(name="Juan Perez", uid='1234', email = "email@pagnia.com.ar")
        aCourse.student_set.add(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertTrue(aCourse.student_set.contains(aStudent), 'Set, expected to contain Juan Perez')
        
        aCourse.student_set.remove(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertFalse(aCourse.student_set.contains(aStudent), 'Set, expected to have no Juan Perez student')
    
    def testCourseAddAssignment(self):
        """
        I will take a course and add an assignment to it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')
        assignment = Practice.objects.get_or_create(uid="LPC", course=aCourse, file="pathfile", deadline="2012-12-01")
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertTrue(aCourse.practice_set.contains(assignment), 'Set, expected to contain LPC')
    
    def testCourseDeleteAssignment(self):
        """
        I will take a course and remove an assignment from it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')
        assignment = Practice.objects.get_or_create(uid="LPC", course=aCourse, file="pathfile", deadline="2012-12-01")
        self.assertTrue(aCourse.practice_set.contains(assignment), 'Set, expected to contain LPC')
        assignment.delete()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertFalse(aCourse.practice_set.contains(assignment), 'Set, not expected to contain LPC')
    
