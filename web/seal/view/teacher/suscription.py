# -*- coding=utf-8 -*-

from django.shortcuts import render
from seal.model import Suscription, Student
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.context import RequestContext
from seal.model.shift import Shift
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE
from seal.model.course import Course
from django.http import HttpResponseRedirect
from seal.view.teacher import user_is_teacher

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def listsuscription(request, idcourse, idshift):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    shift = Shift.objects.get(pk=idshift)
    suscriptions = Suscription.objects.filter(shift=shift, state="Pending").order_by('suscriptionDate')
    suscriptions_solve = Suscription.objects.filter(shift=shift).order_by('suscriptionDate')
    suscriptions_solve = suscriptions_solve.exclude(state="Pending")
    return render(request, 'suscription/listsuscription.html', 
                  {'current_course' : current_course,
                   'courses' : courses, 'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'shift': shift}, 
                  context_instance=RequestContext(request))

REDIRECT_PENDING_SUSCRIPTIONS = "/teacher/suscription/listsuscriptionpending/"

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def acceptgroup(request, idcourse):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    suscription_list = request.POST.getlist('suscription')
    for suscrip_id in suscription_list:
        suscription = Suscription.objects.get(pk=suscrip_id)
        suscription.state = "Accept"
        suscription.resolveDate = date.today()
        suscription.save()
        student = Student.objects.get(pk=suscription.student.pk)
        student.shifts.add(suscription.shift)
    return HttpResponseRedirect(REDIRECT_PENDING_SUSCRIPTIONS + str(current_course.pk))

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def rejectgroup(request, idcourse):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    suscription_list = request.POST.getlist('suscription')
    for suscrip_id in suscription_list:
        suscription = Suscription.objects.get(pk=suscrip_id)
        suscription.state = "Reject"
        suscription.resolveDate = date.today()
        suscription.save()
    return HttpResponseRedirect(REDIRECT_PENDING_SUSCRIPTIONS + str(current_course.pk))

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def listsuscriptionpending(request, idcourse):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)

    shifts = Shift.objects.filter(course = current_course)
    table_suscription_shift = []
    for shift in shifts:
        suscriptionPending = shift.suscription_set.filter(state='pending')
        if suscriptionPending:
            table_suscription_shift.append({'shift':shift, 'suscriptionPending':suscriptionPending})
    
    suscriptions = Suscription.objects.filter(shift__course=current_course, state="Pending").order_by('suscriptionDate')
    suscriptions_solve = Suscription.objects.filter(shift__course=current_course).order_by('suscriptionDate')
    suscriptions_solve = suscriptions_solve.exclude(state="Pending")
    
    return render(request, 'suscription/listsuscriptionpending.html', 
                  {'current_course' : current_course,
                   'courses' : courses, 'table_suscription_shift': table_suscription_shift,
                   'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve}, context_instance=RequestContext(request))    
        
        