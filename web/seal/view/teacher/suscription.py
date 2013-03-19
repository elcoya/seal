from django.shortcuts import render
from seal.model import Suscription, Student
from datetime import date
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from seal.model.shift import Shift
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def listsuscription(request, idshift):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        shift = Shift.objects.get(pk=idshift)
        suscriptions = Suscription.objects.filter(shift=shift, state="Pending").order_by('suscriptionDate')
        suscriptions_solve = Suscription.objects.filter(shift=shift).order_by('suscriptionDate')
        suscriptions_solve = suscriptions_solve.exclude(state="Pending")
        return render(request, 'suscription/listsuscription.html', 
                      {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'shift': shift}, 
                      context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def acceptgroup(request, idshift):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        suscription_list = request.POST.getlist('suscription')
        shift = Shift.objects.get(pk=idshift)
        for suscrip_id in suscription_list:
            suscription = Suscription.objects.get(pk=suscrip_id)
            suscription.state = "Accept"
            suscription.resolveDate = date.today()
            suscription.save()
            student = Student.objects.get(pk=suscription.student.pk)
            student.shifts.add(shift)
        suscriptions = Suscription.objects.filter(shift=shift, state="Pending").order_by('suscriptionDate')
        suscriptions_solve = Suscription.objects.filter(shift=shift).order_by('suscriptionDate')
        suscriptions_solve = suscriptions_solve.exclude(state="Pending")
        return render(request, 'suscription/listsuscription.html', 
                      {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'shift': shift}, 
                      context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def rejectgroup(request, idshift):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        suscription_list = request.POST.getlist('suscription')
        shift = Shift.objects.get(pk=idshift)   
        for suscrip_id in suscription_list:
            suscription = Suscription.objects.get(pk=suscrip_id)
            suscription.state = "Reject"
            suscription.resolveDate = date.today()
            suscription.save()
        suscriptions = Suscription.objects.filter(shift=shift, state="Pending").order_by('suscriptionDate')
        suscriptions_solve = Suscription.objects.filter(shift=shift).order_by('suscriptionDate')
        suscriptions_solve = suscriptions_solve.exclude(state="Pending")
        return render(request, 'suscription/listsuscription.html', 
                      {'suscriptions': suscriptions, 'suscriptionsSolve': suscriptions_solve, 'shift': shift}, 
                      context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def listsuscriptionpending(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        shifts = Shift.objects.all()
        table_suscription_shift = []
        for shift in shifts:
            suscriptionPending = shift.suscription_set.filter(state='pending')
            if suscriptionPending:
                table_suscription_shift.append({'shift':shift, 'suscriptionPending':suscriptionPending})
        return render(request, 'suscription/listsuscriptionpending.html', 
                      {'table_suscription_shift': table_suscription_shift}, context_instance=RequestContext(request))    
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
        
        