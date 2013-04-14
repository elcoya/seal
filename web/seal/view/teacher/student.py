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
from seal.model.automatic_correction import AutomaticCorrection
from seal.model.course import Course
from seal.model.practice import Practice
from seal.model.shift import Shift
from seal.model.delivery import Delivery
from seal.model.correction import Correction
from django.contrib.auth.decorators import login_required
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE
from seal.model.mail import Mail
from seal.forms.studentSearch import StudentSearchForm
from django.db.models import Q

PATHOK = "/teacher/students/list/%s"
PATHOKENROLED = "/teacher/students/"
MAXPAGINATOR = 10

SUBJECTMAILCREATE = "Creacion de usuario en ALGO3"
BODYMAILCREATE = "Se creo un usuario en ALGO3 para ti. Tu informacion de ingreso es Padron: %s y Password: %s"


@login_required
def index(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
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
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def newstudent(request, idshift):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
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
                
                mail = Mail()
                mail.save_mail(SUBJECTMAILCREATE, BODYMAILCREATE % (user.username, form.data['passwd']), user.email)
                return HttpResponseRedirect(PATHOK % str(idshift))
        else:
            form = StudentForm(initial={'shifts': [idshift]})
        return render(request, 'student/new-student.html', {'form': form, 'idshift': idshift}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def editstudent(request, idshift, idstudent):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        student = Student.objects.get(pk=idstudent)     
        if (request.method == 'POST'):
            form = StudentForm(request.POST, instance=student,
                               initial={'email': student.user.email, 'first_name': student.user.first_name, 'last_name': student.user.last_name})
            
            if (form.is_valid()):
                if (form.data['passwd'] != ''):
                    student.user.set_password(form.data['passwd'])
                student.user.email = form.data['email']
                student.user.first_name = form.data['first_name']
                student.user.last_name = form.data['last_name']
                student.user.save()
                form.save()
                return HttpResponseRedirect(PATHOK % str(idshift))
        else:
            form = StudentForm(instance=student, initial={'email': student.user.email, 'first_name': student.user.first_name, 'last_name': student.user.last_name})
        return render(request, 'student/editstudent.html', {'form': form, 'idshift': idshift}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def edit_unenrolled_student(request, idstudent):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        student = Student.objects.get(pk=idstudent)     
        if (request.method == 'POST'):
            form = StudentForm(request.POST, instance=student)
            if (form.is_valid()):
                form.save()
                return HttpResponseRedirect(PATHOKENROLED)
        else:
            form = StudentForm(instance=student)
        return render(request, 'student/editstudent.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def pendingdeliveries(request, idcourse):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        current_course = courses.get(pk=idcourse)
        
        final_list = []
        #TAKE ALL COURSES ACTIVOS
        practices = current_course.get_practices()
        #RECORRO TOAS LAS PRACITAS DEL CURSO
        for practice in practices:
            shifts = Shift.objects.filter(course=current_course)
            student_shift_list = []
            #RECORRO TODOS LOS TURNOS DEL CURSO
            for shift in shifts:
                #TOMO LOS ESTUDIANTES DEL TURNO
                students = shift.get_students()
                for student in students:
                    #TODO LAS ENTREGAS DEL ESTUDIANTE PARA ESA PRACTICA
                    deliveries = Delivery.objects.filter(student=student, practice=practice)
                    appendStudent = True;
                    #ME FIJO SI ALGUNA TIENE SUCCESSFULL, SI ES ASI NO LA ADJUNTO A LA LISTA
                    for delivery in deliveries:
                        if delivery.get_automatic_correction().get_status() == AutomaticCorrection.STATUS_STRINGS[1]:
                            appendStudent = False;
                    if (appendStudent):
                        student_shift_list.append({'student': student, 'shift':shift})
            if len(student_shift_list) > 0:
                final_list.append({'practice': practice, 'student_shift_list':student_shift_list})            
        return render(request, 'student/delivery_pending.html', 
                      {'current_course' : current_course,
                       'courses' : courses,
                       'final_list': final_list})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def list_student(request, idcourse):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        current_course = courses.get(pk=idcourse)

        students = Student.objects.filter(shifts__course = current_course).order_by('uid')
        listable_students = []
        for student in students:
            student_dict = {'pk' : student.pk,
                            'uid' : student.uid,
                            'full_name' : student.get_full_name(),
                            'email' : student.user.email,
                            'shift' : student.get_shift(current_course),}
            if student.corrector is not None:
                student_dict.update({'corrector' : student.corrector.user.last_name})
            listable_students.append(student_dict)
        return render(request, 'student/liststudent.html', 
                      {'current_course' : current_course,
                       'courses' : courses, 
                       'students': listable_students}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def list_student_deliveries(request, idcourse, idstudent):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        current_course = courses.get(pk=idcourse)

        student = Student.objects.get(pk=idstudent)
        deliveries = Delivery.objects.filter(student=student, practice__course=current_course).order_by('deliverDate')
        table_deliveries = []
        for delivery in deliveries:
            correction = Correction.objects.filter(delivery=delivery)
            table_deliveries.append({'delivery': delivery, 'correction':correction})
        return render(request, 'student/liststudentdeliveries.html', 
                      {'current_course' : current_course,
                       'courses' : courses, 
                       'table_deliveries': table_deliveries, 'student':student}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def studentsearch(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        form = StudentSearchForm()
        students = []
        if (request.method == 'POST'):
            form = StudentSearchForm(request.POST)
            data = form.data['data_search']
            students = Student.objects.filter(Q(uid__icontains = data) | Q(user__first_name__icontains = data) | 
                                                  Q(user__last_name__icontains = data))
        return render(request,'student/studentsearch.html', {'query':data, 'students': students})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def studentdetail(request, idstudent):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        student = Student.objects.get(pk=idstudent)
        return render(request, 'student/detail.html', {'student':student}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
    