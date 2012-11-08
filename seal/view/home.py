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
from django.contrib.auth import authenticate, logout
from seal.forms.login import LoginForm
from django.contrib.auth.decorators import login_required
from seal.model.teacher import Teacher

@login_required
def index(request):
    print "index: redirecting..."
    user = request.user
    print str(user.id)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin')
    elif(Teacher.objects.filter(user_id=user.id)):
        return HttpResponseRedirect('/teacher')
    elif(Student.objects.filter(user_id=user.id).exists()):
        return HttpResponseRedirect('/undergraduate')
    else:
        return render_to_response('index.html')

@login_required
def redirect(request):
    print "redirect: redirecting..."
    user = request.user
    if(user.is_superuser):
        return HttpResponseRedirect('/admin')
    elif(Teacher.objects.filter(user_id=user.id).exists()):
        return HttpResponseRedirect('/teacher')
    else:
        return HttpResponseRedirect('/undergraduate')

def register(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            user = User()
            user.username = form.data['uid']
            user.last_name = form.data['name']
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

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

