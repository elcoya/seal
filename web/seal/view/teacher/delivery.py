from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from seal.model import Practice, Delivery
from django.contrib.auth.decorators import login_required
from zipfile import ZipFile
from seal.utils import managepath
import os

TYPEZIP = "application/zip"

@login_required
def listdelivery(request, idpractice):
    practice = Practice.objects.get(pk=idpractice)
    deliveries = Delivery.objects.filter(practice=practice).order_by('deliverDate')
    return render(request, 'delivery/listdelivery.html', {'deliveries': deliveries , 'practice': practice,})

@login_required
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
            files_list.append(filename)
        else:
            files_list.append(os.path.join(relative_path, filename))
    for directory in directories:
        if(relative_path is None):
            walk_directory(files_list, os.path.join(path, directory), directory)
        else:
            walk_directory(files_list, os.path.join(path, directory), os.path.join(relative_path, directory))

@login_required
def browse(request, iddelivery, file_to_browse=None):
    print "file: " + str(file_to_browse)
    delivery = Delivery.objects.get(pk=iddelivery);
    extraction_dir = os.path.join(managepath.get_instance().get_workspace_proyect_path(), str(delivery.pk))
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
                  {'delivery': delivery, 'files_list': files_list, 'file_content': file_content})

@login_required
def explore(request, iddelivery):
    return browse(request, iddelivery)

@login_required
def detail(request, iddelivery):
    delivery = Delivery.objects.get(pk=iddelivery);
    return render(request, 'delivery/deliverydetail.html', {'delivery': delivery})

