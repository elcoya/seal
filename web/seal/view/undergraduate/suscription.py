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

@login_required
def index(request):
    student = request.user.student_set.get(uid=request.user.username)
    suscriptions = Suscription.objects.filter(student = student).order_by('suscriptionDate')
    
    courses = Course.objects.all()
    student_courses = student.courses.all()
    courses_student_pending = []
    suscript_pending = suscriptions.filter(state = "Pending")
    for sus_pen in suscript_pending:
        courses_student_pending.append(sus_pen.course)
            
    course_to_suscript = list(set(courses) - set(student_courses) - set(courses_student_pending))    
    
    return render(request, 'suscription/suscription.html', 
                  {'courses': course_to_suscript , 'suscriptions':suscriptions}, 
                  context_instance=RequestContext(request))

@login_required
def newsuscription(request, idcourse):
    student = request.user.student_set.get(uid=request.user.username)
    course = Course.objects.get(pk=idcourse)
    suscription = Suscription(student = student, course = course, state = "Pending", suscriptionDate=date.today())
    suscription.save()
    return HttpResponseRedirect("/undergraduate/suscription")
