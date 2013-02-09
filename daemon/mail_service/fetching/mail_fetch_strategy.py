"""

@author: anibal

"""

class MailFetchStrategy():
    """
    
    Head of the mail fetching strategy. Defines the methods that must be provided in order to obtain the mails which
    are waiting to be sent.
    
    """
    
    def get_pending_mails(self):
        """
        Returns a list of mail entities pending to be send
        """
        yield None
    
