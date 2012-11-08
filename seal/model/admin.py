'''
Created on 07/10/2012

@author: anibal
'''
from seal.model.course import Course
from seal.model.student import Student
from seal.model.practice import Practice
from seal.model.delivery import Delivery
from django.contrib import admin
from seal.model.teacher import Teacher

class CourseAdmin(admin.ModelAdmin):
    ordering = ['-name',]
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
admin.site.register(Practice)
admin.site.register(Delivery)
admin.site.register(Teacher)