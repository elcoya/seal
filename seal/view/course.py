'''
Created on 28/10/2012

@author: martin
'''
from django.http import HttpResponseRedirect
from seal.forms.course import CourseForm
from django.shortcuts import render_to_response, render

def index(request):
    return render_to_response('course/index.html')

def newcourse(request):
    if (request.method=='POST'):
        form = CourseForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course')
    else:
        form = CourseForm()
    return render(request,'course/newcourse.html',{'form': form,})
