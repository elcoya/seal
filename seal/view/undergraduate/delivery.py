from django.http import HttpResponseRedirect
from seal.forms.delivery import DeliveryForm
from django.shortcuts import render
from seal.model import Practice, Delivery, Student
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def newdelivery(request, idpractice):
    idstudent = request.user.student_set.get(uid=request.user.username).pk
    student = Student.objects.get(pk=idstudent)
    practice = Practice.objects.get(pk=idpractice)    
    deliveries = Delivery.objects.filter(student=student, practice=practice)
    if (request.method == 'POST'):
        delivery = Delivery(student=student, practice=practice, deliverDate=date.today())
        form = DeliveryForm(request.POST, request.FILES, instance=delivery)
        if (form.is_valid()):
            form.save()
            pathok = "/undergraduate/practice/list/" + str(practice.course_id)
            return HttpResponseRedirect(pathok)
    else:
        form = DeliveryForm()
    return render(request, 'delivery/uploaddelivery.html', 
                  {'form': form, 'idstudent' : idstudent, 'idcourse' : practice.course_id, 
                   'namepractice':practice.uid, 'deliveries': deliveries})

