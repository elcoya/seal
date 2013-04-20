from django.test import TestCase
from seal.model.course import Course
from seal.model.student import Student
from seal.model.practice import Practice
from seal.model.shift import Shift

class CourseIntegrationTest(TestCase):
    def testCourseUniqueName(self):
        """
        I will try to create a Course with the same name as another and expect a failure
        """
        aName = '2012-2C'
        Course.objects.get_or_create(name=aName)
        course = Course.objects.get(name=aName)
        self.assertEqual(course.name, aName, "course's expected name was '" + aName + "' but actual was '" + course.name + "'")
         
    def testCourseAddAssignment(self):
        """
        I will take a course and add an assignment to it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')[0]
        assignment = Practice.objects.get_or_create(uid="LPC", course=aCourse, deadline="2012-12-01")[0]
        aCourse = Course.objects.get(name='2012-1C')
        self.assertTrue(assignment in aCourse.get_practices(), 'Set, expected to contain LPC')
    
    def testCourseDeleteAssignment(self):
        """
        I will take a course and remove an assignment from it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')[0]
        assignment = Practice.objects.get_or_create(uid="LPC", course=aCourse, deadline="2012-12-01")[0]
        self.assertTrue(assignment in aCourse.get_practices(), 'Set, expected to contain LPC')
        assignment.delete()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertFalse(assignment in aCourse.get_practices(), 'Set, not expected to contain LPC')
    
    
    
    def testCourseGetStudentCountReturnsStudentQueryset(self):
        name = "2012-2C"
        shift_name = 'lunes'
        course = Course.objects.get_or_create(name = name)[0]
        student = Student.objects.get_or_create(uid = '55555')[0]
        shift = Shift.objects.get_or_create(name = shift_name, course = course)[0]
        student.shifts.add(shift)
        shift.save()
        student.save()
        
        count = course.get_student_count()
        self.assertTrue(count > 0)
    
    def testCourseGetStudentCountReturnsEmptyStudentQueryset(self):
        name = "2012-2C"
        course = Course.objects.get_or_create(name = name)[0]
        count = course.get_student_count()
        self.assertEqual(0, count)
    
