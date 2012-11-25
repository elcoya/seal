from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.context import RequestContext
from seal.model.delivery import Delivery

@login_required
def details(request, iddelivery):
    delivery = Delivery.objects.get(pk=iddelivery)
    autocheck = delivery.autocheck_set.all()[0]
    return render(request, 'autocheck/detailsundergraduate.html',
                  {'autocheck': autocheck, 'practice': delivery.practice},
                  context_instance=RequestContext(request))
