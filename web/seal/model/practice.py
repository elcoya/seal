from django.db import models
from seal.model.course import Course
from datetime import date
from seal.model.student import Student
from django.db.models import Q
from django.utils.encoding import smart_str

class Practice(models.Model):
    """Assignment.
    
    This class, probably poorly named, represents the assignments given to the
    Students to do in order to pass the Course.
    
    """
    
    STATUS_SUCCESSFULL = 0
    
    uid = models.CharField(max_length=32,verbose_name="Name")
    course = models.ForeignKey(Course)
    deadline = models.DateField()
    blocker = models.BooleanField()
    
    class Meta:
        """Metadata class indicating how this objects must be unique"""
        unique_together = (("uid", "course"),)
    
    def __str__(self):
        """Stringify the Practice or assignment"""
        return (smart_str(self.uid))
    
    def get_script(self):
        if (not self.script_set.all()):
            return None
        return self.script_set.all()[0]
    
    def delete_script(self):
        self.script_set.all().delete()

    def get_practice_file(self):
        if (not self.practicefile_set.all()):
            return None
        return self.practicefile_set.all()

    def delete_practice_file(self):
        self.practicefile_set.all().delete()

    def isExpired(self):
        if ((self.deadline < date.today()) and self.blocker):
            return True
        else:
            return False

    def get_successfull_deliveries_count(self):
        return self.delivery_set.filter(automaticcorrection__status = 1, practice = self).count()

    def get_failed_deliveries_count(self):
        return self.delivery_set.filter(~Q(automaticcorrection__status = 1), practice = self).count()

    def get_students_pending_deliveries_count(self):
        students = Student.objects.filter(shifts__course = self.course).count()
        students_delivery_succesfull = Student.objects.filter(delivery__automaticcorrection__status = 1, delivery__practice = self).distinct().count()
        return students - students_delivery_succesfull
        
    # for the dashboard view
    def get_completion_percentage(self):
        deliveries_queryset = self.delivery_set.filter(automaticcorrection__status = 1, practice = self).all()
        students = []
        for delivery in deliveries_queryset:
            if delivery.student not in students:
                students.append(delivery.student)
        shifts = self.course.shift_set.all()
        total_students = 0
        for shift in shifts:
            total_students += shift.student_set.all().count()
        if total_students == 0:
            return 0
        return 100 * len(students) / total_students
        
    def get_remaining_percentage(self):
        return 100 - self.get_completion_percentage()
    
    def count_deliveries(self):
        return self.delivery_set.count()
