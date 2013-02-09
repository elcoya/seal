"""

@author: anibal

"""
import smtplib

class MailSessionHelper():
    """
    Head of the preparation strategy class hierarchy
    """
    
    def __init__(self, email_host=None, email_port=None, email_host_user=None, email_host_password=None):
        self.email_host = email_host
        self.email_port = email_port
        self.email_host_user = email_host_user
        self.email_host_pass = email_host_password
        
        self.smtplib = smtplib
    
    def get_server_session(self):
        session = self.smtplib.SMTP(self.email_host, self.email_port) 
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email_host_user, self.email_host_pass)
        return session
    
    def close_server_session(self, session):
        session.quit()
