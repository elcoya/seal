from django.http import HttpResponseRedirect
from django.shortcuts import render
from seal.model import Delivery
from django.template.context import RequestContext
from seal.forms.correction import CorrectionForm
from seal.model import Correction
from django.contrib.auth.decorators import login_required
from seal.utils.managemail import Managemail

PATHREDIRECTINDEX = "/teacher/correction/edit/%s"
PATHOKINDEX = "/teacher/delivery/list/%s"
PATHOKEDITCORRECTION =  "/teacher/delivery/list/%s"
SUBJECTEMAIL = "You have a correction to see on SEAL"
BODYEMAIL = "You have a correction to see in delivery: %s from practice: %s"

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
                sendmail(delivery)
                return HttpResponseRedirect(PATHOKINDEX % str(delivery.practice.pk))
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
            sendmail(correction.delivery)
            return HttpResponseRedirect(PATHOKEDITCORRECTION % str(correction.delivery.practice.pk))
    else:    
        form = CorrectionForm(instance=correction)
    return render(request, 'correction/index.html', 
                  {'form': form, 'delivery': correction.delivery}, 
                  context_instance=RequestContext(request))

def sendmail(delivery):
    managemail = Managemail()
    #managemail.sendmail(SUBJECTEMAIL, BODYEMAIL % (str(delivery.pk), delivery.practice.uid), delivery.student.email) 
    managemail.setSubjet(SUBJECTEMAIL)
    managemail.setRecipient(delivery.student.email)
    managemail.setText(BODYEMAIL % (str(delivery.pk), delivery.practice.uid))
    managemail.sendmail()
