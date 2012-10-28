'''
Created on 25/10/2012

@author: anibal
'''
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from seal.forms.student import StudentForm

def index(request):
    return render_to_response('student/index.html', context_instance=RequestContext(request))

def newstudent(request):
    if (request.method == 'POST'):
        print "Posting student data."
        form = StudentForm(request.POST)
        if (form.is_valid()):
            print "Form is valid."
            form.save()
            return render_to_response('student/student-save-success.html', context_instance=RequestContext(request))
        else:
            print "Form is valid."
            return render_to_response('student/student-action-error.html', {'message': "Can't save student!"}, context_instance=RequestContext(request))
    else:
        print "Method is not POST."
        form = StudentForm()
        return render(request, 'student/new-student.html', {'form': form,}, context_instance=RequestContext(request))
