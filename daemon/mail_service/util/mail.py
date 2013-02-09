"""

@author: anibal

"""

class Mail:
    """
    Utilitary class to represent the mail entities which will be handled by the mail sending process.
    """


    def __init__(self, id=None, recipient=None, subject=None, body=None):
        """
        Constructor
        """
        self.id = id
        self.recipient = recipient
        self.subject = subject
        self.body = body
    
    def __str__(self):
        "id:" + str(self.id) + " - Recipient:" + str(self.recipient) + " - Subject:" + self.subject
    
    def build_to_send_from_host(self, email_host_user):
        headers = ["From: " + email_host_user, 
                   "Subject: " + self.subject,
                   "To: " + self.recipient, 
                   "MIME-Version: 1.0", 
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        return headers + "\r\n\r\n" + self.body

    