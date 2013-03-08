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
from seal.model.innings import Innings

REDIRECTOKNEWSUSCRIPTION = "/undergraduate/suscription"

@login_required
def index(request):
    student = request.user.student_set.get(uid=request.user.username)
    suscriptions = Suscription.objects.filter(student = student).order_by('suscriptionDate')
    
    innings = Innings.objects.all()
    
    student_innings = student.innings.all()
    suscript_pending = suscriptions.filter(state = "Pending")
    
    innings_same_course = []
    for inning in student_innings:
        course = inning.course
        innigns_course = Innings.objects.filter(course=course)
        for inning_same in innigns_course:
            innings_same_course.append(inning_same)
    
    innings_student_pending = []
    for sus_pen in suscript_pending:
        course = sus_pen.inning.course
        innigns_course_pend = Innings.objects.filter(course=course)
        for inning_same_pend in innigns_course_pend:
            innings_student_pending.append(inning_same_pend)
            
    innings_to_suscript = list(set(innings) - set(innings_same_course) - set(innings_student_pending))    
    
    return render(request, 'suscription/suscription.html', 
                  {'innings': innings_to_suscript , 'suscriptions':suscriptions}, 
                  context_instance=RequestContext(request))

@login_required
def newsuscription(request, idinning):
    student = request.user.student_set.get(uid=request.user.username)
    innign = Innings.objects.get(pk=idinning)
    suscription = Suscription(student = student, inning = innign, state = "Pending", suscriptionDate=date.today())
    suscription.save()
    return HttpResponseRedirect(REDIRECTOKNEWSUSCRIPTION)
