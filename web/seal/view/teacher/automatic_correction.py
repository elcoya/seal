from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.template.context import RequestContext
from seal.model.delivery import Delivery
from seal.model.course import Course
from seal.view.teacher import user_is_teacher
#from auto_correction.automatic_correction_runner import AutomaticCorrectionRunner

#@login_required
#def run_automatic_correction_subprocess(request):
#    runner = AutomaticCorrectionRunner()
#    results = runner.run()
#    return render(request, 'automatic_correction/results.html', {'results': results}, 
#                  context_instance=RequestContext(request))

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def details(request, idcourse, iddelivery):
    current_course = Course.objects.get(pk = idcourse)
    courses = Course.objects.all()
    
    delivery = Delivery.objects.get(pk=iddelivery)
    automatic_correction = delivery.get_automatic_correction()
    return render(request, 'automatic_correction/details.html',
                  {'current_course': current_course,
                   'courses': courses,
                   'automatic_correction': automatic_correction, 'practice': delivery.practice},
                  context_instance=RequestContext(request))
    
