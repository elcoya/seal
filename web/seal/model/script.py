from django.db import models
from seal.model.practice import Practice
from seal.utils import managepath
from django.utils.encoding import smart_str

class Script(models.Model):
    """
    
    This class is the holder for the scripts associated with each practice that
    will be run to check the deliveries in an automatic way.
    
    """
    
    practice = models.ForeignKey(Practice, unique=True)
    file = models.FileField(upload_to=managepath.get_instance().get_script_path(), max_length=128)

    def __str__(self):
        return smart_str(self.practice)
