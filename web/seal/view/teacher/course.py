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

PATHOKNEWCOURSE = "/"
MAXPAGINATOR = 25

@login_required
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
def newcourse(request):
    if (request.method=='POST'):
        form = CourseForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CourseForm()
    return render(request, 'course/newcourse.html', {'form': form,})

@login_required
def editcourse(request, idcourse):
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
        students = course.get_students().order_by('name')
        table_students = []
        for student in students:
            table_students.append({'pk': student.pk, 'name': student.name, 'email': student.email, 'uid': student.uid, 'corrector': student.corrector})
    return render(request, 'course/editcourse.html',
                  {'form': form, 'table_contents': table_contents, 'table_students': table_students, 
                   'course': course, 'idcourse': course.pk }, 
                  context_instance=RequestContext(request))
