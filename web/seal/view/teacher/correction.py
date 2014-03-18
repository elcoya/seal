# -*- coding=utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render
from seal.model import Delivery
from django.template.context import RequestContext
from seal.forms.correction import CorrectionForm
from seal.model import Correction
from django.contrib.auth.decorators import login_required, user_passes_test
from seal.model.mail import Mail
from seal.model.teacher import Teacher
from seal.model.course import Course
from seal.view.teacher import user_is_teacher

PATHREDIRECTINDEX = "/teacher/correction/edit/%s/%s"
#PATHOK = "/teacher/delivery/list/%s"
#SUBJECTEMAIL = "You have a correction to see on SEAL"
#BODYEMAIL = "You have a correction to see in delivery: %s from practice: %s. Coment: %s. Grade: %s"

PATH_DASHBOARD = "/teacher/%s"

SUBJECTEMAIL = "Tienes una correccion para ver en Jarvis"
BODYEMAIL = "Tienes una correccion para ver en la entrega: %s de la practica: %s. Comentario: %s. Nota: %s"


@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def index(request, idcourse, iddelivery):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    delivery = Delivery.objects.get(pk=iddelivery)
    correction = Correction.objects.filter(delivery=delivery)
    corrector = ""
    if len(correction) != 0:
        return HttpResponseRedirect(PATHREDIRECTINDEX % (current_course.pk, str(correction[0].pk)))
    else:
        if (request.method == 'POST'):
            correction = Correction(delivery=delivery)
            teacher = Teacher.objects.get(user=request.user)
            correction.corrector = teacher
            corrector = correction.corrector
            form = CorrectionForm(request.POST, instance=correction)
            if (form.is_valid()):
                form.save()
                mail = Mail()
                mail.save_mail(SUBJECTEMAIL, BODYEMAIL % (str(correction.delivery.pk), correction.delivery.practice.uid, form.data['publicComent'], form.data['grade']), correction.delivery.student.user.email)
                return HttpResponseRedirect(PATH_DASHBOARD % current_course.pk)

        else:
            form = CorrectionForm()
        return render(request, 'correction/index.html', 
                      {'current_course' : current_course,
                       'courses' : courses,
                       'form': form, 'delivery': delivery, 'corrector': corrector}, context_instance=RequestContext(request))


@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def editcorrection(request, idcourse, idcorrection):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    correction = Correction.objects.get(pk=idcorrection)
    if (request.method == 'POST'):
        teacher = Teacher.objects.get(user=request.user)
        correction.corrector = teacher
        form = CorrectionForm(request.POST, instance=correction)
        if (form.is_valid()):
            form_edit = form.save(commit=False)
            form_edit.save()
            mail = Mail()
            mail.save_mail(SUBJECTEMAIL, BODYEMAIL % (str(correction.delivery.pk), 
                                                      correction.delivery.practice.uid, 
                                                      form.data['publicComent'], 
                                                      form.data['grade']), 
                           correction.delivery.student.user.email)
            return HttpResponseRedirect(PATH_DASHBOARD % current_course.pk)

    else:    
        form = CorrectionForm(instance=correction)
    return render(request, 'correction/index.html',
                  {'current_course' : current_course,
                   'courses' : courses,
                   'form': form, 'delivery': correction.delivery, 'corrector': correction.corrector},
                  context_instance=RequestContext(request))
