'''
Created on 05/11/2012

@author: anibal
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    return render_to_response('student/index.html', context_instance=RequestContext(request))


