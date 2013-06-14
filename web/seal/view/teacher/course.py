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
from django.contrib.auth.decorators import login_required, user_passes_test
import os
from seal.model.shift import Shift
from seal.view.teacher import user_is_teacher

PATHOKNEWCOURSE = "/"
PATH_DASHBOARD = "/teacher/%s"
MAXPAGINATOR = 25

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def index(request):
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

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def newcourse(request, idcourse=None):
    courses = Course.objects.all()
    if idcourse is not None:
        current_course = courses.get(pk=idcourse)
    else:
        current_course = None
    
    if (request.method == 'POST'):
        form = CourseForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(PATH_DASHBOARD % form.instance.pk)
    else:
        form = CourseForm()
    return render(request, 'course/newcourse.html', 
                  {'current_course' : current_course,
                   'courses' : courses,
                   'form': form, })

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def editcourse(request, idcourse):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    course = current_course
    if (request.method == 'POST'):
        form = CourseForm(request.POST, instance=course)
        if (form.is_valid()):
            form_edit = form.save(commit=False)
            form_edit.save()
            return HttpResponseRedirect(PATH_DASHBOARD % course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/editcourse.html',
                  {'current_course' : current_course,
                   'courses' : courses,
                   'form': form, 'course': course},
                  context_instance=RequestContext(request))


@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def detailcourse(request, idcourse):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    course = Course.objects.get(pk=idcourse)
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
    table_shifts = []
    shifts = Shift.objects.filter(course=course)
    for shift in shifts:
        count = shift.get_students_count()
        table_shifts.append({'shift': shift, 'count': count})
            
    return render(request, 'course/detailcourse.html',
                  {'current_course' : current_course,
                   'courses' : courses,
                   'table_contents': table_contents, 'table_shifts': table_shifts,
                   'course': course},
                  context_instance=RequestContext(request))
