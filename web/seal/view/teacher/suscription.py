from django.shortcuts import render
from seal.model import Course, Suscription, Student
from datetime import date
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

@login_required
def listsuscription(request, idcourse):
    course = Course.objects.get(pk=idcourse)
    suscriptions = Suscription.objects.filter(course=course, state="Pending").order_by('suscriptionDate')
    suscriptions_solve = Suscription.objects.filter(course=course).order_by('suscriptionDate')
    suscriptions_solve = suscriptions_solve.exclude(state="Pending")
    return render(request, 'suscription/listsuscription.html', 
                  {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'course': course}, 
                  context_instance=RequestContext(request))

@login_required
def acceptgroup(request, idcourse):
    suscription_list = request.POST.getlist('suscription')
    course = Course.objects.get(pk=idcourse)
    for suscrip_id in suscription_list:
        suscription = Suscription.objects.get(pk=suscrip_id)
        suscription.state = "Accept"
        suscription.resolveDate = date.today()
        suscription.save()
        student = Student.objects.get(pk=suscription.student.pk)
        student.courses.add(course)
    suscriptions = Suscription.objects.filter(course=course, state="Pending").order_by('suscriptionDate')
    suscriptions_solve = Suscription.objects.filter(course=course).order_by('suscriptionDate')
    suscriptions_solve = suscriptions_solve.exclude(state="Pending")
    return render(request, 'suscription/listsuscription.html', 
                  {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'course': course}, 
                  context_instance=RequestContext(request))

@login_required
def rejectgroup(request, idcourse):
    suscription_list = request.POST.getlist('suscription')
    course = Course.objects.get(pk=idcourse)   
    for suscrip_id in suscription_list:
        suscription = Suscription.objects.get(pk=suscrip_id)
        suscription.state = "Reject"
        suscription.resolveDate = date.today()
        suscription.save()
    suscriptions = Suscription.objects.filter(course=course, state="Pending").order_by('suscriptionDate')
    suscriptions_solve = Suscription.objects.filter(course=course).order_by('suscriptionDate')
    suscriptions_solve = suscriptions_solve.exclude(state="Pending")
    return render(request, 'suscription/listsuscription.html', 
                  {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'course': course}, 
                  context_instance=RequestContext(request))
