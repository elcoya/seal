"""

@author: anibal

"""
from seal.model.delivery import Delivery
from seal.model.automatic_correction import AutomaticCorrection
from django.db.models import F
from django.db.models import Q

class DbDeliveriesExtractor:
    
    STATUS_TRANSLATION_DICTIONARY = {-1: "desaprobado", 1: "aprobado"}
    
    def __init__(self):
        self.objects = Delivery.objects
    
    def get_data(self):
        # Django magic... don't touch unless you fully understand it
        successfull = self.objects.filter(automaticcorrection__status=AutomaticCorrection.STATUS_SUCCESSFULL,
                                          student__pk=F('student__pk'), pk__gte=F('pk'))
        failed = self.objects.filter((~Q(student__delivery__automaticcorrection__status=AutomaticCorrection.STATUS_SUCCESSFULL)),
                                     automaticcorrection__status=AutomaticCorrection.STATUS_FAILED,
                                     student__pk=F('student__pk'), pk__gte=F('pk'),
                                    )
        result = []
        for delivery in successfull:
            correction = delivery.get_correction()
            if correction is not None:
                grade = correction.grade
            else:
                grade = None
            result.append((delivery.practice.uid, delivery.student.uid, delivery.student.user.first_name, delivery.student.user.last_name, 
                           DbDeliveriesExtractor.STATUS_TRANSLATION_DICTIONARY[delivery.get_automatic_correction().status],
                           grade))
        
        for delivery in failed:
            correction = delivery.get_correction()
            if correction is not None:
                grade = correction.grade
            else:
                grade = None
            result.append((delivery.practice.uid, delivery.student.uid, delivery.student.user.first_name, delivery.student.user.last_name, 
                           DbDeliveriesExtractor.STATUS_TRANSLATION_DICTIONARY[delivery.get_automatic_correction().status],
                           grade))
        
        return result

