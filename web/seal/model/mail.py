from django.db import models

class Mail(models.Model):
    """
    
    Mail objects are the entities which represents the mail to send.
    
    """
    STATUS_STRINGS = {0:"pending", 1:"send"}
    STATUS_UNKNOWN = 'unknown status'
    
    subject = models.CharField(max_length=300)
    body = models.CharField(max_length=10240, blank=True)
    recipient = models.EmailField()
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return ("Mail to " + self.recipient + " - status: " + self.get_status())
    
    def get_status(self):
        """Returns a status raw value as a human readable value"""
        try:
            status_string = Mail.STATUS_STRINGS[self.status]
        except:
            status_string = Mail.STATUS_UNKNOWN
        return status_string
    
    def save_mail(self, subject, body, recipient):
        self.body = body
        self.recipient = recipient
        self.subject = subject
        self.status = 0
        self.save()
        