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
from seal.forms.script import PracticeScriptForm
from seal.model.script import Script

PATHOK =  "/teacher/course/editcourse/%s"
MAXPAGINATOR = 10

@login_required
def index(request):
    practice_list = Practice.objects.all().order_by('-deadline')
    paginator = Paginator(practice_list, MAXPAGINATOR) # Show 10 practice per page
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
            return HttpResponseRedirect(PATHOK % str(idcourse))
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
            return HttpResponseRedirect(PATHOK % str(idcourse))
    else:
        form = PracticeForm(instance=practice)
    return render(request, 'practice/editpractice.html', {'form': form, 'idcourse': idcourse,}, context_instance=RequestContext(request))

@login_required
def script(request, idcourse , idpractice):
    practice = Practice.objects.get(pk=idpractice)
    script_text = ''
    if (request.method == 'POST'):
        if (Script.objects.filter(practice=practice).exists()):
            script_instance = Script.objects.get(practice=practice)
        else:
            script_instance = Script(practice=practice)
        form = PracticeScriptForm(request.POST, request.FILES, instance=script_instance)
        if (form.is_valid()):
            form_edit = form.save(commit=False)
            form_edit.save()
            return HttpResponseRedirect(PATHOK % str(idcourse))
    else:
        if(practice.get_script()):
            form = PracticeScriptForm(instance=practice.get_script())
            script_file = open(practice.get_script().file.name, "r")
            script_text = script_file.read()
            script_file.close()
        else:
            form = PracticeScriptForm()
    return render(request, 'practice/script.html', 
                  {'form': form, 'practice': practice, 'idcourse': idcourse, 'script_text': script_text}, 
                  context_instance=RequestContext(request))
