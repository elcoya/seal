'''
Created on 20/11/2012

@author: martin
'''
from django.core.mail import EmailMessage

class Managemail(object):
    
    def __init__(self):
        self.email = EmailMessage()
        
    def setSubjet(self, subject):
        self.email.subject = subject;
    
    def setText(self, text):
        self.email.body = text
    
    def setRecipient(self, recipient):
        self.email.to = [recipient,]
    
    def sendmail(self):
        self.email.send()