from django.shortcuts import render
from seal.model import Suscription, Student
from datetime import date
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from seal.model.innings import Innings

@login_required
def listsuscription(request, idinning):
    inning = Innings.objects.get(pk=idinning)
    suscriptions = Suscription.objects.filter(inning=inning, state="Pending").order_by('suscriptionDate')
    suscriptions_solve = Suscription.objects.filter(inning=inning).order_by('suscriptionDate')
    suscriptions_solve = suscriptions_solve.exclude(state="Pending")
    return render(request, 'suscription/listsuscription.html', 
                  {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'inning': inning}, 
                  context_instance=RequestContext(request))

@login_required
def acceptgroup(request, idinning):
    suscription_list = request.POST.getlist('suscription')
    inning = Innings.objects.get(pk=idinning)
    for suscrip_id in suscription_list:
        suscription = Suscription.objects.get(pk=suscrip_id)
        suscription.state = "Accept"
        suscription.resolveDate = date.today()
        suscription.save()
        student = Student.objects.get(pk=suscription.student.pk)
        student.innings.add(inning)
    suscriptions = Suscription.objects.filter(inning=inning, state="Pending").order_by('suscriptionDate')
    suscriptions_solve = Suscription.objects.filter(inning=inning).order_by('suscriptionDate')
    suscriptions_solve = suscriptions_solve.exclude(state="Pending")
    return render(request, 'suscription/listsuscription.html', 
                  {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'inning': inning}, 
                  context_instance=RequestContext(request))

@login_required
def rejectgroup(request, idinning):
    suscription_list = request.POST.getlist('suscription')
    inning = Innings.objects.get(pk=idinning)   
    for suscrip_id in suscription_list:
        suscription = Suscription.objects.get(pk=suscrip_id)
        suscription.state = "Reject"
        suscription.resolveDate = date.today()
        suscription.save()
    suscriptions = Suscription.objects.filter(inning=inning, state="Pending").order_by('suscriptionDate')
    suscriptions_solve = Suscription.objects.filter(inning=inning).order_by('suscriptionDate')
    suscriptions_solve = suscriptions_solve.exclude(state="Pending")
    return render(request, 'suscription/listsuscription.html', 
                  {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'inning': inning}, 
                  context_instance=RequestContext(request))
