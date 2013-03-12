from django.shortcuts import render
from seal.model import Suscription, Student
from datetime import date
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from seal.model.innings import Innings
from seal.settings import HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def listsuscription(request, idinning):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        inning = Innings.objects.get(pk=idinning)
        suscriptions = Suscription.objects.filter(inning=inning, state="Pending").order_by('suscriptionDate')
        suscriptions_solve = Suscription.objects.filter(inning=inning).order_by('suscriptionDate')
        suscriptions_solve = suscriptions_solve.exclude(state="Pending")
        return render(request, 'suscription/listsuscription.html', 
                      {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'inning': inning}, 
                      context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def acceptgroup(request, idinning):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
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
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def rejectgroup(request, idinning):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
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
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def listsuscriptionpending(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        innings = Innings.objects.all()
        table_suscription_inning = []
        for inning in innings:
            suscriptionPending = inning.suscription_set.filter(state='pending')
            if suscriptionPending:
                table_suscription_inning.append({'inning':inning, 'suscriptionPending':suscriptionPending})
        return render(request, 'suscription/listsuscriptionpending.html', 
                      {'table_suscription_inning': table_suscription_inning}, context_instance=RequestContext(request))    
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
        
        