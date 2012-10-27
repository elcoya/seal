'''
Created on 25/10/2012

@author: anibal
'''
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from seal.forms.student import StudentForm

def index(request):
    return render_to_response('student/index.html')

def newstudent(request):
    if (request.method == 'POST'):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect('/students')
    else:
        form = StudentForm()
    return render(request, 'student/new-student.html', {'form': form,})