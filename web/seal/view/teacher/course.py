'''
Created on 28/10/2012

@author: martin
'''
from django.http import HttpResponseRedirect
from seal.forms.course import CourseForm
from django.shortcuts import render_to_response, render
from seal.model import Course, Delivery
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
import os
from seal.model.innings import Innings
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE

PATHOKNEWCOURSE = "/"
MAXPAGINATOR = 25

@login_required
def index(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses_list = Course.objects.all().order_by('-name')
        paginator = Paginator(courses_list, MAXPAGINATOR) # Show 25 courses per page
        page = request.GET.get('page')
        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            courses = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            courses = paginator.page(paginator.num_pages)
        return render_to_response('course/index.html', {"courses": courses}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def newcourse(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        if (request.method=='POST'):
            form = CourseForm(request.POST)
            if (form.is_valid()):
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = CourseForm()
        return render(request, 'course/newcourse.html', {'form': form,})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def editcourse(request, idcourse):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        course = Course.objects.get(pk=idcourse)     
        if (request.method == 'POST'):
            form = CourseForm(request.POST, instance = course)
            if (form.is_valid()):
                form_edit = form.save(commit=False)
                form_edit.save()
                return HttpResponseRedirect(PATHOKNEWCOURSE)
        else:
            form = CourseForm( instance = course)
            practices = course.get_practices().order_by('deadline')
            table_contents = []
            for practice in practices:
                ndeliveries = Delivery.objects.filter(practice=practice.pk).count()
                if (practice.get_script()):
                    script = practice.get_script()
                    table_contents.append({'pk': practice.pk, 
                                           'uid': practice.uid, 
                                           'deadline': practice.deadline, 
                                           'ndeliveries':  ndeliveries, 
                                           'script': os.path.basename(script.file.name)})
                else:
                    table_contents.append({'pk': practice.pk, 'uid': practice.uid, 'deadline': practice.deadline, 
                                           'ndeliveries':  ndeliveries})
            table_innings = []
            innings = Innings.objects.filter(course=course)
            for inning in innings:
                count = inning.get_students_count()
                table_innings.append({'inning': inning, 'count': count})
                
        return render(request, 'course/editcourse.html',
                      {'form': form, 'table_contents': table_contents, 'table_innings': table_innings, 
                       'course': course, 'idcourse': course.pk }, 
                      context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
