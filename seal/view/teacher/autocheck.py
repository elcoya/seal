from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from seal.daemon.daemon import AutocheckRunner
from django.template.context import RequestContext

@login_required
def run_autocheck_subprocess(request):
    runner = AutocheckRunner()
    results = runner.run()
    return render(request, 'teacher/autocheck/results.html', {'results': results}, 
                  context_instance=RequestContext(request))

