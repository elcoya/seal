'''
Created on 25/10/2012

@author: anibal
'''
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from seal.forms.student import StudentForm, Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from seal.model.innings import Innings
from seal.model.delivery import Delivery
from seal.model.correction import Correction
from django.contrib.auth.decorators import login_required

PATHOK = "/teacher/students/list/%s"
PATHOKENROLED = "/teacher/students/"
MAXPAGINATOR = 10

@login_required
def index(request):
    student_list = Student.objects.all().order_by('uid')
    paginator = Paginator(student_list, MAXPAGINATOR) # Show 10 practice per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
    return render_to_response('student/index.html', {"students": students}, context_instance=RequestContext(request))

@login_required
def newstudent(request, idinning):
    if (request.method == 'POST'):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            user = User()
            user.username = form.data['uid']
            user.set_password(form.data['passwd'])
            user.email = form.data['email']
            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']
            user.save()
            form.instance.user = user
            form.save()
            return HttpResponseRedirect(PATHOK % str(idinning))
    else:
        form = StudentForm(initial={'innings': [idinning]})
    return render(request, 'student/new-student.html', {'form': form, 'idinning': idinning}, context_instance=RequestContext(request))

@login_required
def editstudent(request, idinning, idstudent):
    student = Student.objects.get(pk=idstudent)     
    if (request.method == 'POST'):
        form = StudentForm(request.POST, instance = student, 
                           initial = {'email': student.user.email, 'first_name': student.user.first_name, 'last_name': student.user.last_name})
        
        if (form.is_valid()):
            if (form.data['passwd']!=''):
                student.user.set_password(form.data['passwd'])
            student.user.email = form.data['email']
            student.user.first_name = form.data['first_name']
            student.user.last_name = form.data['last_name']
            student.user.save()
            form.save()
            return HttpResponseRedirect(PATHOK % str(idinning))
    else:
        form = StudentForm(instance = student, initial = {'email': student.user.email, 'first_name': student.user.first_name, 'last_name': student.user.last_name})
    return render(request, 'student/editstudent.html', {'form': form, 'idinning': idinning}, context_instance=RequestContext(request))

@login_required
def edit_unenrolled_student(request, idstudent):
    student = Student.objects.get(pk=idstudent)     
    if (request.method == 'POST'):
        form = StudentForm(request.POST, instance = student)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(PATHOKENROLED)
    else:
        form = StudentForm( instance = student)
    return render(request, 'student/editstudent.html', {'form': form}, context_instance=RequestContext(request))


def list_student(request, idinning):
    inning = Innings.objects.get(pk=idinning)
    students = inning.get_students().order_by('uid')
    return render(request, 'student/liststudent.html', {'students': students, 'inning':inning}, context_instance=RequestContext(request))

def list_student_deliveries(request, idstudent, idinning):
    student = Student.objects.get(pk=idstudent)
    inning = Innings.objects.get(pk=idinning)
    deliveries = Delivery.objects.filter(student=student).order_by('deliverDate')
    table_deliveries = []
    for delivery in deliveries:
        correction = Correction.objects.filter(delivery=delivery)
        table_deliveries.append({'delivery': delivery, 'correction':correction})
    return render(request, 'student/liststudentdeliveries.html', {'table_deliveries': table_deliveries, 'student':student, 'inning':inning}, context_instance=RequestContext(request))
    