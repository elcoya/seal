'''
Created on 06/03/2013

@author: martin
'''
from seal.model.innings import Innings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from seal.model.course import Course
from seal.forms.inning import InningForm

PATHOKNEWCOURSE = "/teacher/course/editcourse/%s"

@login_required
def editinning(request, idinning):
    inning = Innings.objects.get(pk=idinning)     
    if (request.method == 'POST'):
        form = InningForm(request.POST, instance = inning)
        if (form.is_valid()):
            form_edit = form.save(commit=False)
            form_edit.save()
            return HttpResponseRedirect(PATHOKNEWCOURSE % inning.course.id)
    else:
        form = InningForm(instance = inning)
    return render(request, 'inning/editinning.html', {'form': form, 'idcourse':inning.course.id})
        
        
@login_required
def newinning(request, idcourse):
    course = Course.objects.get(pk=idcourse)
    if (request.method=='POST'):
        form = InningForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(PATHOKNEWCOURSE % course.id)
    else:
        form = InningForm(initial={'course':course})
    return render(request, 'inning/newinning.html', {'form': form, 'idcourse':idcourse})