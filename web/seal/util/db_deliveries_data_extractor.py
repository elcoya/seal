"""

@author: anibal

"""
from seal.model.delivery import Delivery
from seal.model.automatic_correction import AutomaticCorrection
from django.db.models import F
from django.db.models import Q
from seal.model.course import Course

class DbDeliveriesExtractor:
    
    STATUS_TRANSLATION_DICTIONARY = {-1: "desaprobado", 1: "aprobado"}
    
    def __init__(self):
        self.objects = Delivery.objects
        try:
            self.course = Course.objects.all().latest("name") #aggregate(Max("name"))["name__max"]
        except:
            self.course = None
    
    def get_data(self):
        # Django magic... don't touch unless you fully understand it
        successfull = self.objects.filter(automaticcorrection__status=AutomaticCorrection.STATUS_SUCCESSFULL, practice__course=self.course)
        successfull = successfull.order_by('-pk')
        
        failed = self.objects.filter((~Q(student__delivery__automaticcorrection__status=AutomaticCorrection.STATUS_SUCCESSFULL)),
                                     automaticcorrection__status=AutomaticCorrection.STATUS_FAILED, practice__course=self.course
                                    )
        failed = failed.order_by('-pk')
        
        uid_set = []
        result = []
        for delivery in successfull:
            correction = delivery.get_correction()
            if correction is not None:
                grade = correction.grade
            else:
                grade = None
            if delivery.student.uid not in uid_set:
                result.append((delivery.practice.uid, delivery.student.uid, delivery.student.user.first_name, delivery.student.user.last_name, 
                               DbDeliveriesExtractor.STATUS_TRANSLATION_DICTIONARY[delivery.get_automatic_correction().status],
                               grade))
                uid_set.append(delivery.student.uid)
        
        for delivery in failed:
            correction = delivery.get_correction()
            if correction is not None:
                grade = correction.grade
            else:
                grade = None
            if delivery.student.uid not in uid_set:
                result.append((delivery.practice.uid, delivery.student.uid, delivery.student.user.first_name, delivery.student.user.last_name, 
                               DbDeliveriesExtractor.STATUS_TRANSLATION_DICTIONARY[delivery.get_automatic_correction().status],
                               grade))
                uid_set.append(delivery.student.uid)
        
        return result

