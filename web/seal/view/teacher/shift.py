# -*- coding=utf-8 -*-

'''
Created on 06/03/2013

@author: martin
'''
from seal.model.shift import Shift
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from seal.model.course import Course
from seal.forms.shift import ShiftForm
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE
from seal.view.teacher import user_is_teacher

PATHOKNEWCOURSE = "/teacher/course/detailcourse/%s"
PATH_LIST_SHIFT = "/teacher/students/listshift/%s/%s"
PATH_DASHBOARD = "/teacher/%s"

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def editshift(request, idcourse, idshift):
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
        
@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def newshift(request, idcourse):
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

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def deleteshift(request, idshift):
    shift = Shift.objects.get(pk=idshift)     
    list_student = shift.get_students()
    if (list_student):
        return HTTP_401_UNAUTHORIZED_RESPONSE
    shift.delete()    
    return HttpResponseRedirect(PATHOKNEWCOURSE % str(shift.course.pk))
    