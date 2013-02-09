"""

@author: anibal

"""
import json
from mail_service.util.mail import Mail

class JSONToMailTranslator():
    """
    Helper class to parse json strings retrieved from the rest api into mail entities
    """


    def __init__(self, json_str=None):
        """
        Constructor
        """
        self.json = json_str
    
    def get_mails_list(self):
        mails_data_list = json.loads(self.json)['results']
        mails_list = []
        for mail_data in mails_data_list:
            mail = Mail()
            mail.id = mail_data['id']
            mail.recipient = mail_data['recipient']
            mail.subject = mail_data['subject']
            mail.body = mail_data['body']
            mails_list.append(mail);
        return mails_list
