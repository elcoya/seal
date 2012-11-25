'''
Created on 28/10/2012

@author: martin
'''
from django.http import HttpResponseRedirect
from seal.forms.course import CourseForm
from django.shortcuts import render
from seal.model import Course, Delivery
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def newcourse(request):
    if (request.method=='POST'):
        form = CourseForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CourseForm()
    return render(request, 'course/newcourse.html', {'form': form, })

@login_required
def editcourse(request, idcourse):
    course = Course.objects.get(pk = idcourse)
    if (request.method=='POST'):
        form = CourseForm(request.POST, instance = course)
        if (form.is_valid()):
            form_edit = form.save(commit=False)
            form_edit.save()
            return HttpResponseRedirect('/')
    else:
        form = CourseForm( instance = course)
        practices = course.practice_set.all().order_by('deadline')
        table_contents = []
        for practice in practices:
            ndeliveries = Delivery.objects.filter(practice=practice.pk).count()
            table_contents.append({'pk': practice.pk, 'uid': practice.uid, 'deadline': practice.deadline, 'ndeliveries':  ndeliveries})
        students = course.student_set.all().order_by('name')
        table_students = []
        for student in students:
            table_students.append({'pk': student.pk, 'name': student.name, 'email': student.email, 'uid': student.uid})
    return render(request, 'course/editcourse.html',
                  {'form': form,  'table_contents': table_contents, 'table_students': table_students, 
                   'coursename': course.name, 'idcourse': course.pk}, 
                  context_instance=RequestContext(request))
