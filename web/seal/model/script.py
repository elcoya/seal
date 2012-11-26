from django.db import models
import os
from seal.model.practice import Practice

import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('seal/web/conf/local.cfg'))
BASE_PATH = config.get("Path", "path.workspace")

class Script(models.Model):
    """
    
    This class is the holder for the scripts associated with each practice that
    will be run to check the deliveries in an automatic way.
    
    """
    
    practice = models.ForeignKey(Practice, unique=True)
    file = models.FileField(upload_to=BASE_PATH + "autocheck_scripts/", max_length=128)

    def __str__(self):
        return str(self.practice) + " - " + os.path.basename(self.file.name)
