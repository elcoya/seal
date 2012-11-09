'''
Created on 09/11/2012

@author: martin
'''
from django.shortcuts import render
from seal.model import Course
from django.contrib.auth.decorators import login_required
from seal.model.suscription import Suscription
from django.http import HttpResponseRedirect
from datetime import date

@login_required
def index(request):
    student = request.user.student_set.get(uid=request.user.username)
    suscriptions = Suscription.objects.filter(student = student).order_by('suscriptionDate')
    #TODO: deberia ser courses = all -(student.course.all() + suscription.course) no todos.
    courses = Course.objects.all()
    return render(request, 'undergraduate/suscription.html', {'courses': courses,'suscriptions':suscriptions})

def newsuscription(request, idcourse):
    student = request.user.student_set.get(uid=request.user.username)
    course = Course.objects.get(pk=idcourse)
    suscription = Suscription(student = student, course = course, state = "Pending", suscriptionDate=date.today())
    suscription.save()
    return HttpResponseRedirect("/undergraduate")
