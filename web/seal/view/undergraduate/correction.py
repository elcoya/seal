from django.shortcuts import render
from seal.model import Delivery
from seal.model import Correction
from django.contrib.auth.decorators import login_required

@login_required
def consultcorrection(request, iddelivery):
    delivery = Delivery.objects.get(pk=iddelivery)
    correction = Correction.objects.filter(delivery=delivery)
    return render(request, 'correction/consult.html', {'correction': correction, 'delivery': delivery})
