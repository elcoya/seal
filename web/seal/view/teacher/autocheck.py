from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from seal.daemon.autocheck_runner import AutocheckRunner
from django.template.context import RequestContext
from seal.model.delivery import Delivery

@login_required
def run_autocheck_subprocess(request):
    runner = AutocheckRunner()
    results = runner.run()
    return render(request, 'autocheck/results.html', {'results': results}, 
                  context_instance=RequestContext(request))

@login_required
def details(request, iddelivery):
    delivery = Delivery.objects.get(pk=iddelivery)
    autocheck = delivery.autocheck_set.all()[0]
    return render(request, 'autocheck/details.html',
                  {'autocheck': autocheck, 'practice': delivery.practice},
                  context_instance=RequestContext(request))
    
