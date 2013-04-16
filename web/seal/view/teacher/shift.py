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
PATH_LIST_SHIFT = "/teacher/students/listshift/%s/%s"
PATH_DASHBOARD = "/teacher/%s"

@login_required
def editshift(request, idcourse, idshift):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        course = Course.objects.get(pk=idcourse)
        courses = Course.objects.all()
        
        shift = Shift.objects.get(pk=idshift)     
        if (request.method == 'POST'):
            form = ShiftForm(request.POST, instance = shift)
            if (form.is_valid()):
                form_edit = form.save(commit=False)
                form_edit.save()
                return HttpResponseRedirect(PATH_LIST_SHIFT % (course.pk, shift.pk))
        else:
            form = ShiftForm(instance = shift)
        return render(request, 'shift/editshift.html', 
                      {'current_course': course,
                       'courses': courses,
                       'shift': shift,
                       'form': form, 'idcourse':shift.course.id})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
        
        
@login_required
def newshift(request, idcourse):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        course = Course.objects.get(pk=idcourse)
        courses = Course.objects.all()
        if (request.method=='POST'):
            course = Course.objects.get(pk = idcourse)
            shift = Shift(course = course)
            form = ShiftForm(request.POST, instance = shift)
            if (form.is_valid()):
                shift.save()
                return HttpResponseRedirect(PATH_DASHBOARD % course.id)
        else:
            form = ShiftForm(initial={'course':course})
        return render(request, 'shift/newshift.html', 
                      {'current_course': course,
                       'courses': courses,
                       'form': form, 'idcourse':idcourse})
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
    