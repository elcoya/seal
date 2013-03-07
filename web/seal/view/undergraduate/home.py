'''
Created on 05/11/2012

@author: anibal
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if(request.user.student_set.all()): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        innings = request.user.student_set.get(uid=request.user.username).innings.all()
    return render_to_response('undergraduate/index.html', {'innings': innings}, context_instance=RequestContext(request))


