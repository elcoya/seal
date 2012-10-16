'''
Created on 07/10/2012

@author: anibal
'''
from seal.model.course import Course
from seal.model.student import Student
from django.contrib import admin

class CourseAdmin(admin.ModelAdmin):
    ordering = ['-name',]
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)