'''
Created on 26/10/2012

@author: anibal
'''
from django.shortcuts import render_to_response, render
from seal.model.course import Course
from django.template.context import RequestContext
from seal.forms.registration import RegistrationForm
from seal.model.student import Student
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from seal.forms.login import LoginForm

def index(request):
    courses = Course.objects.all()
    table_contents = []
    for course in courses:
        table_contents.append({'pk': course.pk, 'name': course.name, 'count':course.student_set.count()})
    return render_to_response('index.html', {'table_contents': table_contents}, context_instance=RequestContext(request))

def register(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            user = User()
            user.username = form.data['uid']
            user.set_password(form.data['passwd'])
            user.email = form.data['email']
            user.save()
            student = Student()
            student.user = user
            student.name = form.data['name']
            student.uid = form.data['uid']
            student.email = form.data['email']
            student.save()
            return render(request, 'registration/registration-success.html', context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form}, context_instance=RequestContext(request))


def login(request):
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        username = form.data.username
        password = form.data.password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/student')
            else:
                form.non_field_errors.add('This user is no longer active')
        else:
            form.non_field_errors.add('Invalid login')
