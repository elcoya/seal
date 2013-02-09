'''
Created on 07/02/2013

@author: martin
'''

from rest_framework import serializers
from seal.model.mail import Mail
from seal.model.automatic_correction import AutomaticCorrection
from seal.model.delivery import Delivery
from seal.model.practice import Practice
from seal.model.script import Script


class MailSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Mail
        fields = ('id', 'subject', 'body', 'recipient')
        
class AutomaticCorrectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AutomaticCorrection
        fields = ('id', 'delivery', 'captured_stdout', 'exit_value', 'status')

class DeliverySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Delivery
        fields = ('id', 'file', 'student', 'practice', 'deliverDate')

class PracticeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Practice
        fields = ('id', 'uid', 'course', 'file', 'deadline')

class ScriptSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Script
        fields = ('id', 'practice', 'file')
