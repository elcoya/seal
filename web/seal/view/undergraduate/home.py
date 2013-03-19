'''
Created on 05/11/2012

@author: anibal
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def index(request):
    if(len(request.user.student_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        shifts = request.user.student_set.get(uid=request.user.username).shifts.all()
        return render_to_response('undergraduate/index.html', {'shifts': shifts}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE


