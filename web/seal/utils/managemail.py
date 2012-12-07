'''
Created on 20/11/2012

@author: martin
'''
from django.core.mail import EmailMessage

class Managemail(object):
    
    def sendmail(self, subject, text, recipient):
        email = EmailMessage(subject, text, to=[recipient])
        email.send()