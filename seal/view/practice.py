'''
Created on 23/10/2012

@author: martin
'''
from django.http import HttpResponse, HttpResponseRedirect
from seal.forms.practice import PracticeForm
from django.shortcuts import render
from decimal import Context
from django.template.context import RequestContext

def index(request):
    html = "<html><body> PAGINA PRINCIPAL DE TPS </body></html>"
    return HttpResponse(html)

def newpractice(request):
    if request.method=='POST':
        form = PracticeForm(request.POST)
        if (form.is_valid()):
            #form.save()
            return HttpResponseRedirect('/admin/model/practice/')
    else:
        form = PracticeForm()
    return render(request,'practice/uploadpractice.html',{'form': form,})
