'''
Created on 07/10/2012

@author: anibal
'''
from seal.model.course import Course
from seal.model.student import Student
from seal.model.practice import Practice
from seal.model.delivery import Delivery
from seal.model.automatic_correction import AutomaticCorrection
from django.contrib import admin
from seal.model.teacher import Teacher

class CourseAdmin(admin.ModelAdmin):
    """Utility for Django Admin tools.
    
    Util class that indicates the django admin how to order the courses when 
    listed.
    
    """
    
    ordering = ['-name',]
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
admin.site.register(Practice)
admin.site.register(Delivery)
admin.site.register(AutomaticCorrection)
admin.site.register(Teacher)
