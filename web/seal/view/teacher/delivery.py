# -*- coding=utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from seal.model import Practice, Delivery
from django.contrib.auth.decorators import login_required, user_passes_test
from zipfile import ZipFile
from seal.utils import managepath
import os
from seal.model.student import Student
from seal.model.automatic_correction import AutomaticCorrection
from seal.model.correction import Correction
import shutil
from seal.model.course import Course
from seal.view.teacher import user_is_teacher
from django.utils.encoding import smart_str

TYPEZIP = "application/zip"

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def listdelivery(request, idcourse, idpractice):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    practice = Practice.objects.get(pk=idpractice)
    table_deliveries = []
    deliveries = Delivery.objects.filter(practice=practice).order_by('deliverDate', 'deliverTime')
    for delivery in deliveries:
        correction = Correction.objects.filter(delivery=delivery)
        table_deliveries.append({'delivery': delivery, 'correction':correction})
    return render(request, 'delivery/listdelivery.html', 
                  {'current_course' : current_course,
                   'courses' : courses,
                   'table_deliveries': table_deliveries , 'practice': practice,})

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def listbystudent(request, idcourse, idpractice, idstudent):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    student = Student.objects.get(pk=idstudent)
    practice = Practice.objects.get(pk=idpractice)
    table_deliveries = []
    deliveries = Delivery.objects.filter(practice=practice,student__pk=idstudent)
    for delivery in deliveries:
        correction = Correction.objects.filter(delivery=delivery)
        table_deliveries.append({'delivery': delivery, 'correction':correction})
    return render(request, 'delivery/listdeliveryperstudentperpractice.html', 
                  {'current_course' : current_course,
                   'courses' : courses,
                   'student' : student,
                   'table_deliveries': table_deliveries , 'practice': practice,})

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def download(request, iddelivery):
    delivery = Delivery.objects.get(pk=iddelivery)
    filename = delivery.file.name.split('/')[-1]
    response = HttpResponse(delivery.file, content_type=TYPEZIP)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

def walk_directory(files_list, path, relative_path):
    tuples = []
    for walk_tuple in os.walk(path):
        tuples.append(walk_tuple)
    
    (path, directories, filenames) = tuples[0]
    for filename in filenames:
        if(relative_path is None):
            files_list.append(smart_str(filename))
        else:
            files_list.append(smart_str(os.path.join(relative_path, filename)))
    for directory in directories:
        if(relative_path is None):
            walk_directory(files_list, os.path.join(path, directory), directory)
        else:
            walk_directory(files_list, os.path.join(path, directory), os.path.join(relative_path, directory))

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def browse(request, idcourse, iddelivery, file_to_browse=None):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    delivery = Delivery.objects.get(pk=iddelivery);
    extraction_dir = os.path.join(managepath.get_instance().get_temporary_files_path(), str(delivery.pk))
    if (not os.path.exists(extraction_dir)):
        zipfile = ZipFile(delivery.file)
        zipfile.extractall(extraction_dir)
    
    files_list = []
    walk_directory(files_list, extraction_dir, None)
    
    if (file_to_browse is None):
        file_content = None
    else:
        file_path = os.path.join(extraction_dir, file_to_browse)
        with open(file_path, 'r') as content_file:
            file_content = content_file.read()
    return render(request, 'delivery/browsedelivery.html', 
                  {'current_course' : current_course,
                   'courses' : courses,
                   'delivery': delivery, 'files_list': files_list, 'file_content': smart_str(file_content)})

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def explore(request, idcourse, iddelivery):
    if(os.path.exists(os.path.join(managepath.get_instance().get_temporary_files_path(), str(iddelivery)))):
        shutil.rmtree(os.path.join(managepath.get_instance().get_temporary_files_path(), str(iddelivery)))
    return browse(request, idcourse, iddelivery)

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def detail(request, idcourse, iddelivery):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)
    
    delivery = Delivery.objects.get(pk=iddelivery);
    correction = Correction.objects.filter(delivery=delivery)
    return render(request, 'delivery/deliverydetail.html', 
                  {'current_course' : current_course,
                   'courses' : courses,
                   'delivery': delivery, 'correction':correction})

