'''
Created on 07/02/2013

@author: martin
'''

from rest_framework import generics, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from seal.serializers import MailSerializer
from seal.model.mail import Mail

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'mails': reverse('mail-list', request=request),
        'mails details': reverse('mail-detail', request=request),
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

