from django.db import models
from seal.model.course import Course
#from seal.utils import managepath

class Practice(models.Model):
    """Assignment.
    
    This class, probably poorly named, represents the assignments given to the
    Students to do in order to pass the Course.
    
    """
    uid = models.CharField(max_length=32,verbose_name="Name")
    course = models.ForeignKey(Course)
    #file = models.FileField(upload_to=managepath.get_instance().get_practice_path())
    deadline = models.DateField()
    
    class Meta:
        """Metadata class indicating how this objects must be unique"""
        unique_together = (("uid", "course"),)
    
    def __str__(self):
        """Stringify the Practice or assignment"""
        return (str(self.uid))
    
    def get_script(self):
        if (not self.script_set.all()):
            return None
        return self.script_set.all()[0]
    
    def delete_script(self):
        self.script_set.all().delete()

    def get_practice_file(self):
        if (not self.practicefile_set.all()):
            return None
        return self.practicefile_set.all()

    def delete_practice_file(self):
        self.practicefile_set.all().delete()
    