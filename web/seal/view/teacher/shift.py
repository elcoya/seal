'''
Created on 06/03/2013

@author: martin
'''
from seal.model.shift import Shift
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from seal.model.course import Course
from seal.forms.shift import ShiftForm
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE

PATHOKNEWCOURSE = "/teacher/course/detailcourse/%s"

@login_required
def editshift(request, idshift):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        shift = Shift.objects.get(pk=idshift)     
        if (request.method == 'POST'):
            form = ShiftForm(request.POST, instance = shift)
            if (form.is_valid()):
                form_edit = form.save(commit=False)
                form_edit.save()
                return HttpResponseRedirect(PATHOKNEWCOURSE % shift.course.id)
        else:
            form = ShiftForm(instance = shift)
        return render(request, 'shift/editshift.html', {'form': form, 'idcourse':shift.course.id})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
        
        
@login_required
def newshift(request, idcourse):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        course = Course.objects.get(pk=idcourse)
        if (request.method=='POST'):
            form = ShiftForm(request.POST)
            if (form.is_valid()):
                form.save()
                return HttpResponseRedirect(PATHOKNEWCOURSE % course.id)
        else:
            form = ShiftForm(initial={'course':course})
        return render(request, 'shift/newshift.html', {'form': form, 'idcourse':idcourse})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def deleteshift(request, idshift):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        shift = Shift.objects.get(pk=idshift)     
        list_student = shift.get_students()
        if (list_student):
            return HTTP_401_UNAUTHORIZED_RESPONSE
        shift.delete()    
        return HttpResponseRedirect(PATHOKNEWCOURSE % str(shift.course.pk))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
    