'''
Created on 09/11/2012

@author: martin
'''
from django.shortcuts import render
from seal.model import Course, Suscription
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import date
from django.template.context import RequestContext
from seal.model.shift import Shift

REDIRECTOKNEWSUSCRIPTION = "/undergraduate/suscription"

@login_required
def index(request):
    student = request.user.student_set.get(uid=request.user.username)
    suscriptions = Suscription.objects.filter(student = student).order_by('suscriptionDate')
    
    shifts = Shift.objects.all()
    
    student_shifts = student.shifts.all()
    suscript_pending = suscriptions.filter(state = "Pending")
    
    shifts_same_course = []
    for shift in student_shifts:
        course = shift.course
        innigns_course = Shift.objects.filter(course=course)
        for shift_same in innigns_course:
            shifts_same_course.append(shift_same)
    
    shifts_student_pending = []
    for sus_pen in suscript_pending:
        course = sus_pen.shift.course
        innigns_course_pend = Shift.objects.filter(course=course)
        for shift_same_pend in innigns_course_pend:
            shifts_student_pending.append(shift_same_pend)
            
    shifts_to_suscript = list(set(shifts) - set(shifts_same_course) - set(shifts_student_pending))    
    
    return render(request, 'suscription/suscription.html', 
                  {'shifts': shifts_to_suscript , 'suscriptions':suscriptions}, 
                  context_instance=RequestContext(request))

@login_required
def newsuscription(request, idshift):
    student = request.user.student_set.get(uid=request.user.username)
    innign = Shift.objects.get(pk=idshift)
    suscription = Suscription(student = student, shift = innign, state = "Pending", suscriptionDate=date.today())
    suscription.save()
    return HttpResponseRedirect(REDIRECTOKNEWSUSCRIPTION)
