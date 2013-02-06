from django.http import HttpResponseRedirect
from django.shortcuts import render
from seal.model import Delivery
from django.template.context import RequestContext
from seal.forms.correction import CorrectionForm
from seal.model import Correction
from django.contrib.auth.decorators import login_required
from seal.model.mail import Mail

PATHREDIRECTINDEX = "/teacher/correction/edit/%s"
PATHOK = "/teacher/delivery/list/%s"
SUBJECTEMAIL = "You have a correction to see on SEAL"
BODYEMAIL = "You have a correction to see in delivery: %s from practice: %s. Coment: %s. Grade: %s"

@login_required
def index(request, iddelivery):  
    delivery = Delivery.objects.get(pk=iddelivery)
    correction = Correction.objects.filter(delivery=delivery)
    if len(correction) != 0:
        return HttpResponseRedirect(PATHREDIRECTINDEX % str(correction[0].pk))
    else:
        if (request.method == 'POST'):
            correction = Correction(delivery=delivery)
            form = CorrectionForm(request.POST, instance=correction)
            if (form.is_valid()):
                form.save()
                mail = Mail()
                mail.save_mail(SUBJECTEMAIL, BODYEMAIL % (str(correction.delivery.pk), correction.delivery.practice.uid, form.data['publicComent'], form.data['grade']), correction.delivery.student.email )
                return HttpResponseRedirect(PATHOK % str(delivery.practice.pk))
        else:
            form = CorrectionForm()
        return render(request, 'correction/index.html', {'form': form, 'delivery': delivery}, context_instance=RequestContext(request))

@login_required
def editcorrection(request, idcorrection):
    correction = Correction.objects.get(pk=idcorrection)
    if (request.method == 'POST'):
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
                  {'form': form, 'delivery': correction.delivery}, 
                  context_instance=RequestContext(request))
    