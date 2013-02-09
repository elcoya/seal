'''
Created on 07/02/2013

@author: martin
'''

from rest_framework import generics, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from seal.serializers import MailSerializer, AutomaticCorrectionSerializer,\
    DeliverySerializer, PracticeSerializer, ScriptSerializer
from seal.model.mail import Mail
from seal.model.automatic_correction import AutomaticCorrection
from seal.model.delivery import Delivery
from seal.model.practice import Practice
from seal.model.script import Script

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'mails': reverse('mail-list', request=request),
        'mails details': reverse('mail-detail', request=request),
        'automatic corrections': reverse('automatic_correction-list', request=request),
        'automatic details': reverse('automatic_correction-detail', request=request),
        'delivery corrections': reverse('delivery-list', request=request),
        'delivery details': reverse('delivery-detail', request=request),
        'practice corrections': reverse('practice-list', request=request),
        'practice details': reverse('practice-detail', request=request),
        'script corrections': reverse('script-list', request=request),
        'script details': reverse('script-detail', request=request),
    })

class MailList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of mail.
    """
    queryset = Mail.objects.all()
    serializer_class = MailSerializer

class MailDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = Mail
    serializer_class = MailSerializer

class AutomaticCorrectionList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of automatic corrections.
    """
    queryset = AutomaticCorrection.objects.filter(status=0)
    serializer_class = AutomaticCorrectionSerializer

class AutomaticCorrectionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a list of automatic corrections.
    """
    model = AutomaticCorrection
    serializer_class = AutomaticCorrectionSerializer
    
class DeliveryList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of automatic corrections.
    """
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a list of automatic corrections.
    """
    model = Delivery
    serializer_class = DeliverySerializer

class PracticeList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of automatic corrections.
    """
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer

class PracticeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a list of automatic corrections.
    """
    model = Practice
    serializer_class = PracticeSerializer

class ScriptList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of automatic corrections.
    """
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer

class ScriptDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a list of automatic corrections.
    """
    model = Script
    serializer_class = ScriptSerializer
