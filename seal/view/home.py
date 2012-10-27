'''
Created on 26/10/2012

@author: anibal
'''
from django.shortcuts import render_to_response

def index(request):
    render_to_response('index.html')
