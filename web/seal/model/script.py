from django.db import models
from seal.model.practice import Practice
from seal.utils.managepath import Managepath


class Script(models.Model):
    """
    
    This class is the holder for the scripts associated with each practice that
    will be run to check the deliveries in an automatic way.
    
    """
    
    managepath = Managepath()    
    practice = models.ForeignKey(Practice, unique=True)
    file = models.FileField(upload_to=managepath.get_script_path(), max_length=128)

    def __str__(self):
        return str(self.practice)
