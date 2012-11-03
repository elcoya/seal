'''
Created on 25/10/2012

@author: anibal
'''
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from seal.forms.student import StudentForm, Student

def index(request):
    return render_to_response('student/index.html', context_instance=RequestContext(request))

def newstudent(request, idcourse):
    if (request.method == 'POST'):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            form.save()
            pathok="/course/editcourse/"+str(idcourse)
            return HttpResponseRedirect(pathok)
    else:
        form = StudentForm(initial={'courses': [idcourse]})
    return render(request, 'student/new-student.html', {'form': form, 'idcourse': idcourse}, context_instance=RequestContext(request))

def editstudent(request, idcourse ,idstudent):
    student=Student.objects.get(pk=idstudent)     
    if (request.method=='POST'):
        form = StudentForm(request.POST, instance = student)
        if (form.is_valid()):
            form.save()
            pathok="/course/editcourse/"+str(idcourse)
            return HttpResponseRedirect(pathok)
    else:
        form = StudentForm( instance = student)
    return render(request,'student/editstudent.html',{'form': form, 'idcourse': idcourse}, context_instance=RequestContext(request))