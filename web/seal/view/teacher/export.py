# -*- coding=utf-8 -*-

"""
Created on 18/03/2013

@author: anibal
"""
from django.contrib.auth.decorators import login_required, user_passes_test
from seal.model.course import Course
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from seal.util.db_deliveries_data_extractor import DbDeliveriesExtractor
from seal.utils.csv_tuple_printer import CsvTuplePrinter
from django.http import HttpResponse
from seal.utils.managepath import Managepath
import os
from seal.view.teacher import user_is_teacher

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def choose(request, idcourse):
    courses = Course.objects.all()
    current_course = courses.get(pk=idcourse)

    return render_to_response('export/choose.html', 
                              {'current_course' : current_course,
                               'courses': courses, }, context_instance=RequestContext(request))

TYPECSV = "text/csv"
def get_output_file_name(course_name):
    tmp_path = Managepath().get_temporary_files_path()
    file_name = str(course_name + ".csv")
    return os.path.join(tmp_path, file_name)

@login_required
@user_passes_test(user_is_teacher, login_url='/forbidden/')
def download(request, idcourse):
    course = Course.objects.get(pk=idcourse)
    db_data_extractor = DbDeliveriesExtractor()
    db_data_extractor.course = course
    data = db_data_extractor.get_data()
    csv_tuple_printer = CsvTuplePrinter()
    output_file_name = get_output_file_name(course.name)
    csv_tuple_printer.open(output_file_name)
    for line in data:
        csv_tuple_printer.put(line)
    csv_tuple_printer.close()
    output_file = open(output_file_name)
    response = HttpResponse(output_file, content_type=TYPECSV)
    response['Content-Disposition'] = 'attachment; filename=%s' % output_file_name
    return response

