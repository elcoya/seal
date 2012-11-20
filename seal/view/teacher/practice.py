'''
Created on 23/10/2012

@author: martin
'''
from django.http import HttpResponseRedirect
from seal.forms.practice import PracticeForm
from django.shortcuts import render, render_to_response
from seal.model.practice import Practice
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    practice_list = Practice.objects.all().order_by('-deadline')
    paginator = Paginator(practice_list, 10) # Show 10 practice per page
    page = request.GET.get('page')
    try:
        practices = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        practices = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        practices = paginator.page(paginator.num_pages)
    return render_to_response('practice/index.html', {"practices": practices}, context_instance=RequestContext(request))

@login_required
def newpractice(request, idcourse):
    if (request.method == 'POST'):
        form = PracticeForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            pathok = "/teacher/course/editcourse/" + str(idcourse)
            return HttpResponseRedirect(pathok)
    else:
        form = PracticeForm(initial={'course': idcourse})
    return render(request, 'practice/uploadpractice.html', {'form': form, 'idcourse':idcourse})

@login_required
def editpractice(request, idcourse , idpractice):
    practice = Practice.objects.get(pk=idpractice)     
    if (request.method == 'POST'):
        form = PracticeForm(request.POST, request.FILES, instance=practice)
        if (form.is_valid()):
            form_edit = form.save(commit=False)
            form_edit.save()
            pathok = "/course/editcourse/" + str(idcourse)
            return HttpResponseRedirect(pathok)
    else:
        form = PracticeForm(instance=practice)
    return render(request, 'practice/editpractice.html', {'form': form, 'idcourse': idcourse,}, context_instance=RequestContext(request))

