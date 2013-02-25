from django.http import HttpResponseRedirect
from django.shortcuts import render
from seal.model import Delivery
from django.template.context import RequestContext
from seal.forms.correction import CorrectionForm
from seal.model import Correction
from django.contrib.auth.decorators import login_required
from seal.model.mail import Mail
from seal.model.teacher import Teacher

PATHREDIRECTINDEX = "/teacher/correction/edit/%s"
PATHOK = "/teacher/delivery/list/%s"
SUBJECTEMAIL = "You have a correction to see on SEAL"
BODYEMAIL = "You have a correction to see in delivery: %s from practice: %s. Coment: %s. Grade: %s"

@login_required
def index(request, iddelivery):  
    delivery = Delivery.objects.get(pk=iddelivery)
    correction = Correction.objects.filter(delivery=delivery)
    corrector = ""
    if len(correction) != 0:
        return HttpResponseRedirect(PATHREDIRECTINDEX % str(correction[0].pk))
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
                mail.save_mail(SUBJECTEMAIL, BODYEMAIL % (str(correction.delivery.pk), correction.delivery.practice.uid, form.data['publicComent'], form.data['grade']), correction.delivery.student.email )
                return HttpResponseRedirect(PATHOK % str(delivery.practice.pk))
        else:
            form = CorrectionForm()
        return render(request, 'correction/index.html', {'form': form, 'delivery': delivery, 'corrector': corrector}, context_instance=RequestContext(request))

@login_required
def editcorrection(request, idcorrection):
    correction = Correction.objects.get(pk=idcorrection)
    if (request.method == 'POST'):
        teacher = Teacher.objects.get(user=request.user)
        correction.corrector = teacher
        form = CorrectionForm(request.POST, instance=correction)
        if (form.is_valid()):
            form_edit = form.save(commit=False)
            form_edit.save()
            mail = Mail()
            mail.save_mail(SUBJECTEMAIL, BODYEMAIL % (str(correction.delivery.pk), correction.delivery.practice.uid, form.data['publicComent'], form.data['grade']), correction.delivery.student.email )
            return HttpResponseRedirect(PATHOK % str(correction.delivery.practice.pk))
    else:    
        form = CorrectionForm(instance=correction)
    return render(request, 'correction/index.html', 
                  {'form': form, 'delivery': correction.delivery, 'corrector': correction.corrector}, 
                  context_instance=RequestContext(request))
    