'''
Created on 08/11/2012

@author: anibal
'''
from django.contrib.auth.decorators import login_required
from seal.model.practice_file import PracticeFile
from seal.model.course import Course
from django.shortcuts import render
from django.template.context import RequestContext
from seal.model.practice import Practice
from django.http import HttpResponse

TYPEPDF = "application/pdf"

@login_required
def practicelist(request, idcourse):
    course = Course.objects.get(pk=idcourse)
    practices = course.get_practices().order_by('deadline')
    return render(request, 'practice/practiceList.html', 
                  {'practices': practices, 'coursename': course.name, }, 
                  context_instance=RequestContext(request))

@login_required
def download(request, idpracticefile):
    practicefile = PracticeFile.objects.get(pk=idpracticefile)
    filename = practicefile.file.name.split('/')[-1]
    response = HttpResponse(practicefile.file)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

@login_required
def practiceFilelist(request, idpractice):
    practice = Practice.objects.get(pk = idpractice)
    practiceFiles = practice.get_practice_file()
    return render(request, 'practice/listFile.html', {'practiceFiles': practiceFiles, 'practicename': practice.uid, 'idcourse': practice.course.pk})
