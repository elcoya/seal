'''
Created on 23/10/2012

@author: martin
'''
from django.http import HttpResponseRedirect
from seal.forms.practice import PracticeForm
from seal.model.practice_file import PracticeFile
from django.shortcuts import render, render_to_response
from seal.model.practice import Practice
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from seal.forms.script import PracticeScriptForm
from seal.model.script import Script
from seal.forms.practiceFile import PracticeFileForm
from django.http import HttpResponse
from seal.forms.edit_practice_file import EditPracticeFileForm
import os
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE
from django.utils.encoding import smart_str
from seal.model.delivery import Delivery
from seal.model.course import Course

PATHOK =  "/teacher/course/detailcourse/%s"
PATH_DASHBOARD = "/teacher/%s"
PATHFILEOK = "/teacher/practices/practicefile/%s/%s"
MAXPAGINATOR = 10

@login_required
def index(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
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
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def newpractice(request, idcourse):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        current_course = courses.get(pk=idcourse)
        
        if (request.method == 'POST'):
            course = Course.objects.get(pk = idcourse)
            practice = Practice(course = course)
            form = PracticeForm(request.POST, instance = practice)
            if (form.is_valid()):
                practice.save()
                return HttpResponseRedirect(PATH_DASHBOARD % str(idcourse))
        else:
            form = PracticeForm()
        return render(request, 'practice/uploadpractice.html', 
                      {'current_course' : current_course,
                       'courses' : courses,
                       'form': form, 'idcourse':idcourse})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def editpractice(request, idcourse , idpractice):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        current_course = courses.get(pk=idcourse)
        
        practice = Practice.objects.get(pk=idpractice)     
        if (request.method == 'POST'):
            form = PracticeForm(request.POST, request.FILES, instance=practice)
            if (form.is_valid()):
                form_edit = form.save(commit=False)
                form_edit.save()
                return HttpResponseRedirect(PATH_DASHBOARD % str(idcourse))
        else:
            form = PracticeForm(instance=practice)
        return render(request, 'practice/editpractice.html', 
                      {'current_course' : current_course,
                       'courses' : courses,
                       'form': form, 'idcourse': idcourse,}, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def script(request, idcourse , idpractice):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        current_course = courses.get(pk=idcourse)
        
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
                return HttpResponseRedirect(PATH_DASHBOARD % str(idcourse))
        else:
            if(practice.get_script()):
                form = PracticeScriptForm(instance=practice.get_script())
                script_file = open(practice.get_script().file.name, "r")
                script_text = script_file.read()
                script_file.close()
            else:
                form = PracticeScriptForm()
        return render(request, 'practice/script.html', 
                      {'current_course' : current_course,
                       'courses' : courses,
                       'form': form, 'practice': practice, 'idcourse': idcourse, 'script_text': script_text}, 
                      context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def practicefilelist(request, idcourse, idpractice):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        current_course = courses.get(pk=idcourse)
        
        practice = Practice.objects.get(pk = idpractice)
        practiceFiles = practice.get_practice_file()
        if (request.method == 'POST'):
            practice_file_instance = PracticeFile(practice=practice)
            form = PracticeFileForm(request.POST, request.FILES, instance=practice_file_instance)
            if (form.is_valid()):
                form_edit = form.save(commit=False)
                form_edit.save()
                return HttpResponseRedirect(PATHFILEOK % (str(idcourse), str(practice.pk)))
        else:
            form = PracticeFileForm()
        return render(request, 'practice/uploadFile.html', 
                      {'current_course' : current_course,
                       'courses' : courses,
                       'form': form, 'idcourse':idcourse, 'namepractice':practice.uid, 'practiceFiles': practiceFiles})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def download(request, idpracticefile):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        practicefile = PracticeFile.objects.get(pk=idpracticefile)
        filename = practicefile.file.name.split('/')[-1]
        response = HttpResponse(practicefile.file)
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def delete(request, idpracticefile):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        practicefile = PracticeFile.objects.get(pk=idpracticefile)
        idcourse = practicefile.practice.course.pk
        practice = practicefile.practice
        practicefile.delete()
        return HttpResponseRedirect(PATHFILEOK % (str(idcourse), str(practice.pk)))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

@login_required
def edit(request, idpracticefile):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        practicefile = PracticeFile.objects.get(pk=idpracticefile)
        file_path = practicefile.file.name # os.path.join(extraction_dir, file_to_browse)
        file_basename = os.path.basename(file_path)
        edited = (request.method == 'POST')
        if (request.method == 'POST'):
            form = EditPracticeFileForm(request.POST)
            if (form.is_valid()):
                edited_file_content = smart_str(form.data['content'])
                with open(file_path, 'w') as content_file:
                    content_file.write(edited_file_content)
        else:
            file_content = None
            with open(file_path, 'r') as content_file:
                file_content = content_file.read()
            form = EditPracticeFileForm(initial={'content': smart_str(file_content)})
        return render(request, 'practice/editPracticeFile.html',
                      {'form': form, 'practicefile': practicefile, 'file_basename': file_basename, 'edited': edited})
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE


@login_required
def deletepractice(request, idpractice):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        practice = Practice.objects.get(pk=idpractice)
        delivery_list = Delivery.objects.filter(practice = practice)
        if (delivery_list):
            return HTTP_401_UNAUTHORIZED_RESPONSE
        practice.delete()
        return HttpResponseRedirect(PATH_DASHBOARD % str(practice.course.pk))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

