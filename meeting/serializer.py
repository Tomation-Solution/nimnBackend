from rest_framework import serializers
from . import models
from utils.custom_exceptions import CustomError

from django.shortcuts import get_object_or_404
from account.serializers.user import MemberSerializer


class AdminManageMeetingSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Meeting
        fields = '__all__'
        extra_kwargs  = {
            'chapters':{
                'read_only':True
            }
        }

class MeetingSerializer(serializers.ModelSerializer):
    is_attending= serializers.SerializerMethodField()
    def get_is_attending(self,instance:models.Meeting):
        user = self.context.get('user',None)
        if user is None: return False
        is_attending = instance.meetingattendies_set.filter(members=user.memeber).exists()
        return is_attending
    class Meta:
        model = models.Meeting
        fields = '__all__'

class MeetingRegister(serializers.Serializer):
    meeting = serializers.IntegerField()
    def create(self, validated_data):
        memeber = self.context.get('user').memeber
        meeting =get_object_or_404( models.Meeting,id=validated_data.get('meeting',-1))
        if models.MeetingAttendies.objects.filter(meeting=meeting,members=memeber).exists():CustomError({'error':'You have registered already'})

        meeting_attendies = models.MeetingAttendies.objects.create(
            meeting=meeting
            ,members=memeber)

        return meeting_attendies


class MeetingApologies(serializers.Serializer):
    meeting = serializers.IntegerField()
    note= serializers.CharField()


    def create(self, validated_data):
        memeber = self.context.get('user').memeber
        note = validated_data.get('note','Am sorry i can attend')
        meeting =get_object_or_404( models.Meeting,id=validated_data.get('meeting',-1))
        if models.MeetingApology.objects.filter(meeting=meeting,members=memeber).exists():
            raise CustomError({'error':'You have Sent an apology already'})

        meeting_nonattenders = models.MeetingApology.objects.create(
            meeting=meeting
            ,members=memeber,
            note=note 
            )

        return meeting_nonattenders


class NonattendersMeetingMembersSerializer(serializers.ModelSerializer):
    memeber = serializers.SerializerMethodField()
    def get_memeber(self,meeting_apology:models.MeetingApology):
        clean_data = MemberSerializer(instance=meeting_apology.members,many=False)
        return clean_data.data
    
    

    class Meta:
        model = models.MeetingApology
        fields = ['memeber','id','note','meeting']


class RegisteredMeetingMembersSerializer(serializers.ModelSerializer):

    memebers = serializers.SerializerMethodField()
    def get_memebers(self,meeting):
        return models.MeetingAttendies.objects.filter(
            meeting=meeting
        ).values('id','members__user__email')

    class Meta:
        model = models.Meeting
        fields = [
            'name','date_for','memebers'
        ]


