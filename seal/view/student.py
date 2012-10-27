'''
Created on 25/10/2012

@author: anibal
'''
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from seal.forms.student import StudentForm

def index(request):
    return render_to_response('student/index.html')

def newstudent(request):
    if (request.method == 'POST'):
        form = StudentForm(request.POST)
        form.save()
        render_to_response('student/student-save-success.html')
    else:
        form = StudentForm()
    return render_to_response('student/new-student.html', {'form': form,})
