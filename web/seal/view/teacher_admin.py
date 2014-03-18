# -*- coding=utf-8 -*-

from django.contrib.auth.decorators import permission_required
from seal.forms.teacher import TeacherForm, TeacherModifForm
from seal.model.teacher import Teacher
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from seal.model.mail import Mail

SUBJECTMAILCREATE = "Creacion de usuario en Jarvis"
BODYMAILCREATE = "Se creo un usuario en Jarvis para ti. Ya puedes acceder al sistema con tu login: '%s'/'%s'"

@permission_required('my_custom_perm')
def listteacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'admin/list_teacher.html',
                  {'teachers': teachers }, context_instance=RequestContext(request))


@permission_required('my_custom_perm')
def editteacher(request, idteacher):
    teacher = Teacher.objects.get(pk=idteacher)
    if request.method == 'POST':
        form = TeacherModifForm(request.POST, instance=teacher,
                           initial={'username': teacher.user.username,
                                       'email': teacher.user.email,
                                       'first_name': teacher.user.first_name,
                                       'last_name': teacher.user.last_name})
        if form.is_valid():
            if (form.data['passwd'] != ''):
                teacher.user.set_password(form.data['passwd'])
            if (not User.objects.filter(username = form.data['username']).exists()):
                teacher.user.username = form.data['username']
            teacher.user.email = form.data['email']
            teacher.user.first_name = form.data['first_name']
            teacher.user.last_name = form.data['last_name']
            teacher.user.save()
            form.save()   
            return HttpResponseRedirect('/listteacher')
    else:
        form = TeacherModifForm(instance=teacher,
                            initial={'username': teacher.user.username,
                                       'email': teacher.user.email,
                                       'first_name': teacher.user.first_name,
                                       'last_name': teacher.user.last_name})
    return render_to_response('admin/edit_teacher.html',
                              { 'form': form},
                              context_instance=RequestContext(request))


@permission_required('my_custom_perm')
def newteacher(request):
    if request.method == 'POST':
        # formulario enviado
        form = TeacherForm(request.POST)
        if form.is_valid():
            # formulario validado correctamente
            user = User()
            user.username = form.data['username']
            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']
            user.set_password(form.data['passwd'])
            user.email = form.data['email']
            user.save()
            teacher = Teacher()
            teacher.user = user
            teacher.uid = form.data['uid']
            teacher.appointment = form.data['appointment']
            teacher.save()
            
            mail = Mail()
            mail.save_mail(SUBJECTMAILCREATE, BODYMAILCREATE % (user.username, form.data['passwd']), user.email)
            return HttpResponseRedirect('/listteacher')
    else:
        form = TeacherForm()
    return render_to_response('admin/new_teacher.html',
                              { 'form': form },
                              context_instance=RequestContext(request))
