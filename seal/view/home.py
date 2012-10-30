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
        table_contents.append({course.name : course.student_set.count()})
    print table_contents
    return render_to_response('index.html', {'table_contents': table_contents}, context_instance=RequestContext(request))
