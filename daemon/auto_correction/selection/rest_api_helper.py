"""

@author: anibal

"""
from auto_correction.selection.automatic_correction_selection_strategy import AutomaticCorrectionSelectionStrategy
from auto_correction.log.logger_manager import LoggerManager
import requests
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from auto_correction.selection.json_to_auto_correction_translator import JSONToAutoCorrectionTranslator

class RestApiHelper(AutomaticCorrectionSelectionStrategy):
    """
    Implementation of the selection strategy to perform the search from the web interface
    """
    

    def __init__(self, auth_user, auth_pass, 
                 http_automatic_correction_serializer=None, 
                 http_delivery_serializer=None,
                 http_practice_serializer=None,
                 http_script_serializer=None,
                 http_mail_serializer=None):
        """
        Constructor
        """
        logger_manager = LoggerManager()
        self.log = logger_manager.get_new_logger("auto-correction-strategy")
        self.http_automatic_correction_serializer = http_automatic_correction_serializer
        self.http_delivery_serializer = http_delivery_serializer
        self.http_practice_serializer = http_practice_serializer
        self.http_script_serializer = http_script_serializer
        self.http_mail_serializer = http_mail_serializer
        self.auth_user = auth_user
        self.auth_pass = auth_pass
        
        self.requests = requests
        self.json_translator = JSONToAutoCorrectionTranslator()
    
    def get_automatic_corrections(self):
        self.log.info("Request pending automatic corrections list")
        auto_correction_request = self.requests.get(self.http_automatic_correction_serializer, auth=(self.auth_user, self.auth_pass))
        if (auto_correction_request.status_code == HTTP_200_OK):
            auto_correction_data = auto_correction_request.content
            self.log.debug("request content recived: %s", str(auto_correction_data))
            self.json_translator.json = auto_correction_data
            return self.json_translator.get_automatic_corrections()
        else:
            self.log.debug("request content recived: %s", str(auto_correction_request.status_code))
            return []
    
    def get_delivery(self, pk):
        self.log.debug("Retrieving delivery for id: %d", pk)
        delivery_request = self.requests.get(self.http_delivery_serializer + str(pk), auth=(self.auth_user, self.auth_pass))
        if (delivery_request.status_code == HTTP_200_OK):
            self.log.debug("request content recived: %s", str(delivery_request.content))
            return delivery_request.content
    
    def get_practice(self, pk):
        self.log.debug("Retrieving delivery for id: %d", pk)
        practice_request = self.requests.get(self.http_practice_serializer + str(pk), auth=(self.auth_user, self.auth_pass))
        if (practice_request.status_code == HTTP_200_OK):
            self.log.debug("request content recived: %s", str(practice_request.content))
            return practice_request.content
    
    def get_script(self, pk):
        self.log.debug("Retrieving delivery for id: %d", pk)
        script_request = self.requests.get(self.http_script_serializer + str(pk), auth=(self.auth_user, self.auth_pass))
        if (script_request.status_code == HTTP_200_OK):
            self.log.debug("request content recived: %s", str(script_request.content))
            return script_request.content
    
    def save_automatic_correction(self, automatic_correction):
        self.log.debug("Saving automatic correction through rest api...")
        data = {"id": automatic_correction.pk,
                "delivery": automatic_correction.delivery_id, 
                "exit_value": automatic_correction.exit_value,
                "captured_stdout": automatic_correction.captured_stdout,
                "status": automatic_correction.status}
        self.log.debug("putting request to url: %s", self.http_automatic_correction_serializer)
        self.log.debug("saving data: %s", data)
        response = self.requests.put(self.http_automatic_correction_serializer + str(automatic_correction.pk), data, 
                                 auth=(self.auth_user, self.auth_pass))
        self.log.debug(response)
        self.log.debug(response.content)
        return response
    
    def save_mail(self, mail):
        self.log.info("Posting mail result.")
        data = {"recipient": mail.recipient,
                "subject" : mail.subject,
                "body" : mail.body}
        self.log.debug("Mail data: %s", str(data))
        response = self.requests.post(self.http_mail_serializer, data, auth=(self.auth_user, self.auth_pass))
        self.log.debug(response.content)
        return response
    
#        data = {"id": mail.id, 
#                "recipient": mail.recipient, 
#                "subject": "modified subject"}
#        return self.requests.put(self.http_serializer + str(mail.id), data=data, auth=(self.auth_user, self.auth_pass))

