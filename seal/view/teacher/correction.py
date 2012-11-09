from django.http import HttpResponseRedirect
from django.shortcuts import render
from seal.model import Delivery
from django.template.context import RequestContext
from seal.forms.correction import CorrectionForm
from seal.model import Correction
from django.contrib.auth.decorators import login_required

@login_required
def index(request, iddelivery):  
    delivery = Delivery.objects.get(pk=iddelivery)
    correction = Correction.objects.filter(delivery=delivery)
    if len(correction) != 0: 
        pathredirect = "/teacher/correction/edit/" + str(correction[0].pk)
        return HttpResponseRedirect(pathredirect)
    else:
        if (request.method == 'POST'):
            correction = Correction(delivery=delivery)
            form = CorrectionForm(request.POST, instance=correction)
            if (form.is_valid()):
                form.save()
                pathok = "/teacher/delivery/list/" + str(delivery.practice.pk)
                return HttpResponseRedirect(pathok)
        else:
            form = CorrectionForm()
        return render(request, 'correction/index.html', {'form': form, 'delivery': delivery}, context_instance=RequestContext(request))

@login_required
def editcorrection(request, idcorrection):
    correction = Correction.objects.get(pk=idcorrection)
    if (request.method == 'POST'):
        form = CorrectionForm(request.POST, instance=correction)
        if (form.is_valid()):
            formEdit = form.save(commit=False)
            formEdit.save()
            pathok = "/teacher/delivery/list/" + str(correction.delivery.practice.pk)
            return HttpResponseRedirect(pathok)
    else:    
        form = CorrectionForm(instance=correction)
    return render(request, 'correction/index.html', {'form': form, 'delivery': correction.delivery}, context_instance=RequestContext(request))

