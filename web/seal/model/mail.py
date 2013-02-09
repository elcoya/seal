from django.db import models

class Mail(models.Model):
    """
    
    Mail objects are the entities which represents the mail to send.
    
    """
    subject = models.CharField(max_length=300)
    body = models.CharField(max_length=10240, blank=True)
    recipient = models.EmailField()
    
    def __str__(self):
        return ("Mail to " + self.recipient + " subject - " + self.subject)
      
    def save_mail(self, subject, body, recipient):
        self.body = body
        self.recipient = recipient
        self.subject = subject
        self.save()
        