'''
Created on 07/02/2013

@author: martin
'''

from rest_framework import serializers
from seal.model.mail import Mail


class MailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mail
        fields = ('id', 'subject', 'body', 'recipient')
        