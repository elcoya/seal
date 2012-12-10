'''
Created on 26/10/2012

@author: anibal
'''
from seal.recaptcha.client import captcha
from seal.model.student import Student
from seal.model.teacher import Teacher
from seal.forms.registration import RegistrationForm
from seal.forms.recoverypass import RecoveryForm
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from seal.utils.managemail import Managemail
from seal.forms.changepass import ChangePasswForm

LENGTHPASSWORD = 8
REDIRECTADMIN = "/admin"
REDIRECTTEACHER = "/teacher"
REDIRECTUNDERGRADUATE = "/undergraduate"
REDIRECTINDEX = "index.html"
REDIRECTLOGOUT = "/"
ERRORCAPTCHA = "You Must Be a Robot"

SUBJECTMAIL = "Registration SEAL Successful"
BODYMAIL = "You have been registered in SEAL with username: %s and password: %s"

SUBJECTMAILRECOVERY = "Recovery SEAL Successful"
BODYMAILRECOVERY = "You have requested a password recovery for SEAL. Your new login information is username: %s and new password: %s"

SUBJECTMAILCHANGE = "Change SEAL password Successful"
BODYMAILCHANGE = "You have requested a password change for SEAL. Your new login information is username: %s and new password: %s"


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
                sendmail(user, form.data['passwd'], SUBJECTMAIL, BODYMAIL)
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
                    
def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect(REDIRECTLOGOUT)

def recovery_pass(request):
    if (request.method == 'POST'):
        form = RecoveryForm(request.POST)
        if (form.is_valid()):
            user = User.objects.get(username=form.data['uid'], email=form.data['email'])
            password = random_pass_generate()
            user.set_password(password)
            user.save()
            sendmail(user, password, SUBJECTMAILRECOVERY, BODYMAILRECOVERY)
            return render(request, 'registration/recovery-success.html', context_instance=RequestContext(request))
    else:
        form = RecoveryForm()
    return render(request, 'registration/recovery_pass.html',
                  {'form': form, }, context_instance=RequestContext(request))

def change_password(request):
    if (request.method == 'POST'):
        form = ChangePasswForm(request.POST)
        if (form.is_valid()):
            user = User.objects.get(username=form.data['uid'])
            user.set_password(form.data['passwd'])
            user.save()
            sendmail(user, form.data['passwd'], SUBJECTMAILCHANGE, BODYMAILCHANGE)
            return render(request, 'registration/change-success.html', context_instance=RequestContext(request))
    else:
        form = ChangePasswForm()
    return render(request, 'registration/change_pass.html',
                  {'form': form, }, context_instance=RequestContext(request))
        
def sendmail(user, passw, subject, body):
    managemail = Managemail()
    managemail.set_body(body % (user.username, passw))
    managemail.set_subjet(subject)
    managemail.set_recipient(user.email)
    managemail.sendmail()
    
def random_pass_generate():
    newpass = User.objects.make_random_password(length=LENGTHPASSWORD)
    return newpass
