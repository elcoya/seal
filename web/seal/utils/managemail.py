'''
Created on 20/11/2012

@author: martin
'''
from django.core.mail import EmailMessage

class Managemail(object):
    
    def __init__(self):
        self.email = EmailMessage()
        
    def set_subjet(self, subject):
        self.email.subject = subject
    
    def set_body(self, text):
        self.email.body = text
    
    def set_recipient(self, recipient):
        self.email.to = [recipient,]
    
    def sendmail(self):
        self.email.send()