"""

@author: anibal

"""
from seal.model.delivery import Delivery
from seal.model.automatic_correction import AutomaticCorrection
from django.db.models import F
from django.db.models import Q
from seal.model.course import Course
from seal.model.student import Student
from seal.model.practice import Practice

class DbDeliveriesExtractor:
    
    STATUS_TRANSLATION_DICTIONARY = {-1: "desaprobado", 1: "aprobado"}
    PENDING_STATUS = "pendiente"
    
    def __init__(self):
        self.objects = Delivery.objects
        self.students = Student.objects
        self.practices = Practice.objects
        try:
            self.course = Course.objects.all().latest("name")
        except:
            self.course = None
    
    def get_data(self):
        # Successfull deliveries
        successfull = self.objects.filter(automaticcorrection__status=AutomaticCorrection.STATUS_SUCCESSFULL, practice__course=self.course)
        successfull = successfull.order_by('-deliverDate', '-deliverTime')
        entity_set = []
        result = []
        for delivery in successfull:
            correction = delivery.get_correction()
            if correction is not None:
                grade = correction.grade
            else:
                grade = None
            entity_id = (delivery.practice.uid, delivery.student.uid)
            if entity_id not in entity_set:
                result.append((delivery.practice.uid, delivery.student.uid, delivery.student.user.first_name, delivery.student.user.last_name, 
                               DbDeliveriesExtractor.STATUS_TRANSLATION_DICTIONARY[delivery.get_automatic_correction().status],
                               grade))
                entity_set.append(entity_id)
        
        # Failed deliveries
        failed = self.objects.filter(automaticcorrection__status=AutomaticCorrection.STATUS_FAILED, practice__course=self.course)
        failed = failed.order_by('-deliverDate', '-deliverTime')
        for delivery in failed:
            correction = delivery.get_correction()
            if correction is not None:
                grade = correction.grade
            else:
                grade = None
            entity_id = (delivery.practice.uid, delivery.student.uid)
            if entity_id not in entity_set:
                result.append((delivery.practice.uid, delivery.student.uid, delivery.student.user.first_name, delivery.student.user.last_name, 
                               DbDeliveriesExtractor.STATUS_TRANSLATION_DICTIONARY[delivery.get_automatic_correction().status],
                               grade))
                entity_set.append(entity_id)
        
        # Without deliveries
        #students = self.students.filter(~Q(delivery__isnull=False))
        students = self.students.all().order_by('uid')#.annotate(delivery__isnull=True)
        practices = self.practices.all()
        for student in students:
            for practice in practices:
                entity_id = (practice.uid, student.uid)
                if entity_id not in entity_set:
                    result.append((practice.uid, student.uid, student.user.first_name, student.user.last_name, 
                                   DbDeliveriesExtractor.PENDING_STATUS, None))
                    entity_set.append(entity_id)
        
        # Data sorting
        result.sort(key=lambda delivery: (delivery[0], delivery[1]))
        
        return result

