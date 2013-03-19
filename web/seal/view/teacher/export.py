"""
Created on 18/03/2013

@author: anibal
"""
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE
from django.contrib.auth.decorators import login_required
from seal.model.course import Course
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

@login_required
def choose(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        return render_to_response('export/choose.html', {'courses': courses, }, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def download(request, course_id):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        course = Course.objects.get(pk=course_id)
        
        return render_to_response('export/choose.html', {'courses': courses, }, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

