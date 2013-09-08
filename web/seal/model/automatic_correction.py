from django.db import models
from seal.model.delivery import Delivery
from django.utils.encoding import smart_str

class AutomaticCorrection(models.Model):
    """
    
    AutomaticCorrection objects are the entities which represents the automatic check that
    SEAL can run on the deliveries made by the Students.
    
    """
    
    STATUS_PENDING = 0
    STATUS_FAILED  = -1
    STATUS_SUCCESSFULL = 1
    
    STATUS_STRINGS = {-1:"failed", 0:"pending", 1:"successfull"}
    STATUS_UNKNOWN = 'unknown status'
    
    delivery = models.ForeignKey(Delivery, unique=True)
    captured_stdout = models.CharField(max_length=10240, blank=True)
    exit_value = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        """Stringify the AutomaticCorrection"""
        return ("AutomaticCorrection | exit value: " + str(self.exit_value) + " - status: " + str(self.status))
    
    def get_status(self):
        """Returns a status raw value as a human readable value"""
        try:
            status_string = AutomaticCorrection.STATUS_STRINGS[self.status]
        except:
            status_string = AutomaticCorrection.STATUS_UNKNOWN
        return smart_str(status_string)
    
    def get_delivery_file(self):
        return self.delivery.file.path
    
    def get_correction_script(self):
        script = self.delivery.practice.get_script()
        if script is not None:
            return script.file.path
        else:
            return None
    
    def get_smart_captured_stdout(self):
        return smart_str(self.captured_stdout)
    
    def user_mail(self):
        return self.delivery.student.user.email
    