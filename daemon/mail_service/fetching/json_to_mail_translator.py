"""

@author: anibal

"""
import json
from mail_service.util.mail import Mail
from auto_correction.log.logger_manager import LoggerManager

class JSONToMailTranslator():
    """
    Helper class to parse json strings retrieved from the rest api into mail entities
    """


    def __init__(self, json_str=None):
        """
        Constructor
        """
        self.json = json_str
        logger_manager = LoggerManager()
        self.log = logger_manager.get_new_logger("json translator")
    
    def get_mails_list(self):
        self.log.debug("parsing: %s", self.json)
        mails_data_list = json.loads(self.json)['results']
        mails_list = []
        for mail_data in mails_data_list:
            #self.log("Processing mail data: %s", mail_data)
            mail = Mail()
            mail.id = mail_data['id']
            mail.recipient = mail_data['recipient']
            mail.subject = mail_data['subject']
            mail.body = mail_data['body']
            mails_list.append(mail);
        return mails_list
