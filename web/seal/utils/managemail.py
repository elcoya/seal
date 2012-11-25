'''
Created on 20/11/2012

@author: martin
'''
from django.core.mail import EmailMessage

class Managemail(object):
    
    def sendmail(self, subject, text, email):
        email = EmailMessage(subject, text, to=[email])
        email.send()