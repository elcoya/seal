from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.context import RequestContext
from seal.model.delivery import Delivery

@login_required
def details(request, iddelivery):
    delivery = Delivery.objects.get(pk=iddelivery)
    automatic_correction = delivery.get_automatic_correction()
    return render(request, 'automatic_correction/detailsundergraduate.html',
                  {'automatic_correction': automatic_correction, 'practice': delivery.practice},
                  context_instance=RequestContext(request))
