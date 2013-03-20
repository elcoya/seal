"""
Created on 18/03/2013

@author: anibal
"""
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE
from django.contrib.auth.decorators import login_required
from seal.model.course import Course
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from seal.util.db_deliveries_data_extractor import DbDeliveriesExtractor
from seal.utils.csv_tuple_printer import CsvTuplePrinter
from django.http import HttpResponse
from seal.utils.managepath import Managepath
import os

@login_required
def choose(request):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        courses = Course.objects.all()
        return render_to_response('export/choose.html', {'courses': courses, }, context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE


TYPECSV = "text/csv"
def get_output_file_name(course_name):
    tmp_path = Managepath().get_temporary_files_path()
    file_name = str(course_name + ".csv")
    return os.path.join(tmp_path, file_name)

@login_required
def download(request, idcourse):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
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
        file = open(output_file_name)
        response = HttpResponse(file, content_type=TYPECSV)
        response['Content-Disposition'] = 'attachment; filename=%s' % output_file_name
        return response
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE

