from django.test import TestCase
from seal.model.course import Course
from seal.model.student import Student
from seal.model.practice import Practice

class CourseTest(TestCase):
    def testCourseModelDescription(self):
        """
        Tests __str__
        """
        name = "2012-2C"
        course = Course()
        course.name = name
        assert_name = str(course)
        self.assertEqual(assert_name, name, "Course to string expected to be " + name + " but was " + assert_name)
    
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
        Course.objects.get_or_create(name=aName)
        course = Course.objects.get(name=aName)
        self.assertEqual(course.name, aName, "course's expected name was '" + aName + "' but actual was '" + course.name + "'")
    
    def testCourseAddStudent(self):
        """
        I will take a course and add a student to it. Then, try to get it from the database.
        """
        course_name = '2012-1C'
        aCourse = Course.objects.get_or_create(name=course_name)[0]
        aStudent = Student.objects.get_or_create(name="Juan Perez", uid='1234', email = "email@pagnia.com.ar")[0]
        aCourse.student_set.add(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name=course_name)
        self.assertTrue(aStudent in aCourse.student_set.all(), 'Set, expected to contain Juan Perez')
    
    def testCourseDeleteStudent(self):
        """
        I Will add a Student from a Course and verify it contains the student
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')[0]
        aStudent = Student.objects.get_or_create(name="Juan Perez", uid='1234', email = "email@pagnia.com.ar")[0]
        aCourse.student_set.add(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertTrue(aStudent in aCourse.student_set.all(), 'Set, expected to contain Juan Perez')
        
        aCourse.student_set.remove(aStudent)
        aCourse.save()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertFalse(aStudent in aCourse.student_set.all(), 'Set, expected to have no Juan Perez student')
    
    def testCourseAddAssignment(self):
        """
        I will take a course and add an assignment to it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')[0]
        assignment = Practice.objects.get_or_create(uid="LPC", course=aCourse, file="pathfile", deadline="2012-12-01")[0]
        aCourse = Course.objects.get(name='2012-1C')
        self.assertTrue(assignment in aCourse.practice_set.all(), 'Set, expected to contain LPC')
    
    def testCourseDeleteAssignment(self):
        """
        I will take a course and remove an assignment from it. Then, try to get it from the database.
        """
        aCourse = Course.objects.get_or_create(name='2012-1C')[0]
        assignment = Practice.objects.get_or_create(uid="LPC", course=aCourse, file="pathfile", deadline="2012-12-01")[0]
        self.assertTrue(assignment in aCourse.practice_set.all(), 'Set, expected to contain LPC')
        assignment.delete()
        
        aCourse = Course.objects.get(name='2012-1C')
        self.assertFalse(assignment in aCourse.practice_set.all(), 'Set, not expected to contain LPC')
    
