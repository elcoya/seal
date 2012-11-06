from django.http import HttpResponseRedirect, HttpResponse
from seal.forms.delivery import DeliveryForm
from django.shortcuts import render
from seal.model import Practice, Delivery, Student
from datetime import date

def newdelivery(request, idpractice, idstudent):
    student = Student.objects.get(pk=idstudent)
    practice = Practice.objects.get(pk=idpractice)    
    deliveries = Delivery.objects.filter(student=student,practice=practice)
    if (request.method == 'POST'):
        delivery = Delivery(student=student,practice=practice,deliverDate=date.today())
        form = DeliveryForm(request.POST, request.FILES, instance=delivery)
        for filename, file in request.FILES.iteritems():
            ext = request.FILES[filename].content_type
        if (form.is_valid() and ext == "application/zip"):
            form.save()
            pathok = "/students/practicelist/"+str(practice.course_id)+"/"+str(idstudent)
            return HttpResponseRedirect(pathok)
    else:
        form = DeliveryForm()
    return render(request, 'delivery/uploaddelivery.html', {'form': form, 'idstudent' : idstudent, 'idcourse' : practice.course_id, 'namepractice':practice.uid, 'deliveries': deliveries })

def listdelivery(request, idpractice):
    practice = Practice.objects.get(pk=idpractice)
    deliveries = Delivery.objects.filter(practice=practice).order_by('deliverDate')
    return render(request, 'delivery/listdelivery.html', {'deliveries': deliveries , 'practicename': practice.uid, 'idcourse': practice.course_id })

def download(request, iddelivery):
    delivery = Delivery.objects.get(pk=iddelivery)
    filename = delivery.file.name.split('/')[-1]
    response = HttpResponse(delivery.file, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response