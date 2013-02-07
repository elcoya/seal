'''
Created on 07/02/2013

@author: martin
'''

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from seal.serializers import MailSerializer
from seal.model.mail import Mail


@api_view(['GET'])
def seal_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'mails': reverse('mail-list', request=request),
    })

class MailList(generics.ListCreateAPIView):
    """
    SEAL endpoint that represents a list of mail.
    """
    #model = Mail 
    
    queryset = Mail.objects.filter(status = 0)
    serializer_class = MailSerializer
