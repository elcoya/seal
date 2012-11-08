'''
Created on 05/11/2012

@author: anibal
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from seal.model.course import Course
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    courses = request.user.student_set.get(uid=request.user.username).courses.all()
    table_contents = []
    for course in courses:
        table_contents.append({'pk': course.pk, 'name': course.name})
    return render_to_response('undergraduate/index.html', {'table_contents': table_contents}, context_instance=RequestContext(request))


