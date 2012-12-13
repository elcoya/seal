'''
Created on 08/11/2012

@author: anibal
'''
from django.contrib.auth.decorators import login_required
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
def download(request, idpractice):
    practice = Practice.objects.get(pk=idpractice)
    filename = practice.file.name.split('/')[-1]
    response = HttpResponse(practice.file, content_type=TYPEPDF)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
