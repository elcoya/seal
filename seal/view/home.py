'''
Created on 26/10/2012

@author: anibal
'''
from django.shortcuts import render_to_response
from seal.model.course import Course
from django.template.context import RequestContext

def index(request):
    courses = Course.objects.all()
    table_contents = []
    for course in courses:
        table_contents.append({'pk': course.pk, 'name': course.name, 'count':course.student_set.count()})
    return render_to_response('index.html', {'table_contents': table_contents}, context_instance=RequestContext(request))
