from django.http import HttpResponseRedirect, HttpResponse
from seal.forms.delivery import DeliveryForm
from django.shortcuts import render
from seal.model import Practice, Delivery, Student
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def listdelivery(request, idpractice):
    practice = Practice.objects.get(pk=idpractice)
    deliveries = Delivery.objects.filter(practice=practice).order_by('deliverDate')
    return render(request, 'teacher/listdelivery.html', {'deliveries': deliveries , 'practice': practice,})

@login_required
def download(request, iddelivery):
    delivery = Delivery.objects.get(pk=iddelivery)
    filename = delivery.file.name.split('/')[-1]
    response = HttpResponse(delivery.file, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
