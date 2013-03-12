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
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE

PATHOKNEWCOURSE = "/teacher/course/editcourse/%s"

@login_required
def editinning(request, idinning):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
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
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
        
        
@login_required
def newinning(request, idcourse):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        course = Course.objects.get(pk=idcourse)
        if (request.method=='POST'):
            form = InningForm(request.POST)
            if (form.is_valid()):
                form.save()
                return HttpResponseRedirect(PATHOKNEWCOURSE % course.id)
        else:
            form = InningForm(initial={'course':course})
        return render(request, 'inning/newinning.html', {'form': form, 'idcourse':idcourse})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
    