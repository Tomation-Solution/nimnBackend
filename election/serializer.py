from rest_framework import serializers
from account.models import user as user_models
from utils.custom_exceptions import CustomError
from . import models 

class AdminManageBallotBox(serializers.ModelSerializer):


    class Meta:
        model = models.BallotBox
        fields  = ['name','role_name','role_detail','id',
        'election_startDate',
        'election_endDate',
        'election_endTime',
        'election_startTIme',
        ]

class ContestantCleaner(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self,instance:models.Contestant):
        photo = ''
        try:photo = instance.member.user.photo.url
        except:photo=''

        return {
            'photo':photo
        }

    class Meta:
        model  = models.Contestant
        fields  = [
            'id','member',
            'amount_vote','youtubeVidLink',
            'aspirantBio','upload_manifesto_docs',
            'upload_manifesto_image','user'
        ]
class AdminManageContest(serializers.Serializer):

    "admin manages adding adding and removing members as contestant"
    member =serializers.IntegerField()
    ballotbox =serializers.IntegerField()
    youtubeVidLink = serializers.CharField()
    aspirantBio = serializers.JSONField()
    upload_manifesto_docs = serializers.FileField()
    upload_manifesto_image = serializers.FileField()


    def validate(self, attrs):
        if not user_models.Memeber.objects.filter(id=attrs.get('member')).exists():
            raise serializers.ValidationError({"member":"member does not exist"})
        if not models.BallotBox.objects.filter(id=attrs.get('ballotbox')).exists():
            raise serializers.ValidationError({"ballotbox":"Election does not exist or has ended"})
       
        return super().validate(attrs)
    def create(self, validated_data):
        print("Èhellpow wolrd",validated_data)
        member=user_models.Memeber.objects.get(id=validated_data.get('member'))
        ballotbox = models.BallotBox.objects.get(id=validated_data.get('ballotbox'))
        if models.Contestant.objects.all().filter(member=member,ballotbox=ballotbox).exists():
            raise CustomError({"error":"This Member is Already Contesting For This Election"})
        
        youtubeVidLink =validated_data.get('youtubeVidLink','')
        aspirantBio = validated_data.get('aspirantBio')
        upload_manifesto_docs =validated_data.get('upload_manifesto_docs')
        upload_manifesto_image = validated_data.get('upload_manifesto_image')
        contestant= models.Contestant.objects.create(
            member =member,
            ballotbox =ballotbox,
            amount_vote =0,
            youtubeVidLink=youtubeVidLink,
            aspirantBio =aspirantBio,
            upload_manifesto_docs=upload_manifesto_docs,
            upload_manifesto_image=upload_manifesto_image,
            )
        # contestant.youtubeVidLink = validated_data.get('youtubeVidLink',contestant.youtubeVidLink)

        contestant.save()
        # print(contestant)
        return contestant



class MembersVoteSerializer(serializers.Serializer):
    # contestantID = serializers.IntegerField()
    ballotBoxID = serializers.IntegerField()
    contestantID = serializers.IntegerField()
    vote = serializers.BooleanField()

    def validate(self, attrs):
        if models.BallotBox.objects.all().filter(id=attrs.get('ballotBoxID')).exists():
            # raise CustomError("")
            ballotBox = models.BallotBox.objects.get(id=attrs.get('ballotBoxID'))
            if ballotBox.members_that_has_cast_thier_vote.all().filter(id=self.context.get('member').id).exists():
                "if this user exist in the ballot box that means he has voted"
                raise CustomError({"error":"you can not vote two times"})
        else:
            raise CustomError({"error":"Election Does not exist"})

        return super().validate(attrs)

    # def create(self, validated_data):
    #     contestant = models.Contestant.objects.get(id=validated_data.get('contestantID'))
    #     return super().create(validated_data)
    def update(self, instance, validated_data):
        ballotBox = models.BallotBox.objects.get(id=validated_data.get('ballotBoxID'))
        ballotBox.members_that_has_cast_thier_vote.add(self.context.get('member'))
        instance.amount_vote+=1
        instance.save()
        return instance