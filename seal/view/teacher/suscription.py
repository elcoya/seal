from django.shortcuts import render
from seal.model import Course, Suscription, Student
from datetime import date
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

@login_required
def listsuscription(request, idcourse):
    course = Course.objects.get(pk=idcourse)
    suscriptions = Suscription.objects.filter(course=course, state="Pending").order_by('suscriptionDate')
    suscriptionsSolve = Suscription.objects.filter(course=course).order_by('suscriptionDate')
    suscriptionsSolve = suscriptionsSolve.exclude(state="Pending")
    return render(request, 'teacher/listsuscription.html', {'suscriptions': suscriptions,'suscriptionsSolve': suscriptionsSolve,'course': course}, context_instance=RequestContext(request))

@login_required
def accept(request, idsuscription):
    suscription = Suscription.objects.get(pk=idsuscription)
    suscription.state="Accept"
    suscription.resolveDate = date.today()
    suscription.save()
    
    student = Student.objects.get(pk=suscription.student.pk)
    course = Course.objects.get(pk=suscription.course.pk)
    student.courses.add(course)
    
    suscriptions = Suscription.objects.filter(course=course, state="Pending").order_by('suscriptionDate')
    suscriptionsSolve = Suscription.objects.filter(course=course).order_by('suscriptionDate')
    suscriptionsSolve = suscriptionsSolve.exclude(state="Pending")
    return render(request, 'teacher/listsuscription.html', {'suscriptions': suscriptions,'suscriptionsSolve': suscriptionsSolve,'course': course}, context_instance=RequestContext(request))

@login_required
def reject(request, idsuscription):
    suscription = Suscription.objects.get(pk=idsuscription)
    suscription.state="Reject"
    suscription.resolveDate = date.today()
    suscription.save()
    
    course = Course.objects.get(pk=suscription.course.pk)
    
    suscriptions = Suscription.objects.filter(course=course, state="Pending").order_by('suscriptionDate')
    suscriptionsSolve = Suscription.objects.filter(course=course).order_by('suscriptionDate')
    suscriptionsSolve = suscriptionsSolve.exclude(state="Pending")
    return render(request, 'teacher/listsuscription.html', {'suscriptions': suscriptions,'suscriptionsSolve': suscriptionsSolve,'course': course}, context_instance=RequestContext(request))

@login_required
def acceptGroup(request, idcourse):
    suscriptionList = request.POST.getlist('suscription')
    course = Course.objects.get(pk=idcourse)
    for id in suscriptionList:
        suscription = Suscription.objects.get(pk=id)
        suscription.state="Accept"
        suscription.resolveDate = date.today()
        suscription.save()
        student = Student.objects.get(pk=suscription.student.pk)
        student.courses.add(course)
    suscriptions = Suscription.objects.filter(course=course, state="Pending").order_by('suscriptionDate')
    suscriptionsSolve = Suscription.objects.filter(course=course).order_by('suscriptionDate')
    suscriptionsSolve = suscriptionsSolve.exclude(state="Pending")
    return render(request, 'teacher/listsuscription.html', {'suscriptions': suscriptions,'suscriptionsSolve': suscriptionsSolve,'course': course}, context_instance=RequestContext(request))

@login_required
def rejectGroup(request, idcourse):
    suscriptionList = request.POST.getlist('suscription')
    course = Course.objects.get(pk=idcourse)   
    for id in suscriptionList:
        suscription = Suscription.objects.get(pk=id)
        suscription.state="Reject"
        suscription.resolveDate = date.today()
        suscription.save()
    suscriptions = Suscription.objects.filter(course=course, state="Pending").order_by('suscriptionDate')
    suscriptionsSolve = Suscription.objects.filter(course=course).order_by('suscriptionDate')
    suscriptionsSolve = suscriptionsSolve.exclude(state="Pending")
    return render(request, 'teacher/listsuscription.html', {'suscriptions': suscriptions,'suscriptionsSolve': suscriptionsSolve,'course': course}, context_instance=RequestContext(request))
