'''
Created on 26/10/2012

@author: anibal
'''
from seal.recaptcha.client import captcha
from seal.model.student import Student
from seal.model.teacher import Teacher
from seal.forms.login import LoginForm
from seal.forms.registration import RegistrationForm
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from seal.utils.managemail import Managemail

REDIRECTADMIN = "/admin"
REDIRECTTEACHER = "/teacher"
REDIRECTUNDERGRADUATE = "/undergraduate"
REDIRECTINDEX = "index.html"
ERRORCAPTCHA = "You Must Be a Robot"
SUBJECTMAIL = "Registration SEAL Successful"
BODYMAIL =  "You have been registered in SEAL with username: %s and password: %s"
REDIRECTLOGOUT = "/"

@login_required
def index(request):
    user = request.user
    if(user.is_superuser):
        return HttpResponseRedirect(REDIRECTADMIN)
    elif(Teacher.objects.filter(user_id=user.id)):
        return HttpResponseRedirect(REDIRECTTEACHER)
    elif(Student.objects.filter(user_id=user.id).exists()):
        return HttpResponseRedirect(REDIRECTUNDERGRADUATE)
    else:
        return render_to_response(REDIRECTINDEX)

@login_required
def redirect(request):
    user = request.user
    if(user.is_superuser):
        return HttpResponseRedirect(REDIRECTADMIN)
    elif(Teacher.objects.filter(user_id=user.id).exists()):
        return HttpResponseRedirect(REDIRECTTEACHER)
    else:
        return HttpResponseRedirect(REDIRECTUNDERGRADUATE)

def register(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        check_captcha = captcha.submit(request.POST['recaptcha_challenge_field'],
                                       request.POST['recaptcha_response_field'],
                                       settings.RECAPTCHA_PRIVATE_KEY,
                                       request.META['REMOTE_ADDR'])
        if check_captcha.is_valid:
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
                sendmail(student, form.data['passwd'])
                return render(request, 'registration/registration-success.html', context_instance=RequestContext(request))
        else:
            return render_to_response('registration/register.html', 
                                      {'form': form, 'captcha_publick': settings.RECAPTCHA_PUB_KEY, 
                                       'captcha_response': ERRORCAPTCHA}, 
                                      context_instance=RequestContext(request))  
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', 
                  {'form': form, 'captcha_publick': settings.RECAPTCHA_PUB_KEY}, 
                  context_instance=RequestContext(request))

def sendmail(student, passw):
    managemail = Managemail()
    managemail.sendmail(SUBJECTMAIL, BODYMAIL % (student.uid, passw), student.email)
                
def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect(REDIRECTLOGOUT)
