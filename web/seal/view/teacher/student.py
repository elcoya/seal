'''
Created on 25/10/2012

@author: anibal
'''
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from seal.forms.student import StudentForm, Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

PATHOKNEWSTUDENT = "/teacher/course/editcourse/%s"
PATHOKEDITSTUDENT = "/teacher/course/editcourse/%s"
PATHOKENROLED = "/teacher/students/"
MAXPAGINATOR = 10

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

def newstudent(request, idcourse):
    if (request.method == 'POST'):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(PATHOKNEWSTUDENT % str(idcourse))
    else:
        form = StudentForm(initial={'courses': [idcourse]})
    return render(request, 'student/new-student.html', {'form': form, 'idcourse': idcourse}, context_instance=RequestContext(request))

def editstudent(request, idcourse, idstudent):
    student = Student.objects.get(pk=idstudent)     
    if (request.method == 'POST'):
        form = StudentForm(request.POST, instance = student)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(PATHOKEDITSTUDENT % str(idcourse))
    else:
        form = StudentForm( instance = student)
    return render(request, 'student/editstudent.html', {'form': form, 'idcourse': idcourse}, context_instance=RequestContext(request))

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
