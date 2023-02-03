from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets,permissions,status
from rest_framework.decorators import action
from . import models,serializer
from utils import permissions as custom_permission
from utils import custom_response,custom_exceptions
from account.models import user as user_models
from rest_framework.parsers import  FormParser
from utils import custom_parsers

# Create your views here.



class  AdminManageBallotBox(viewsets.ModelViewSet):
    queryset = models.BallotBox.objects.all()
    serializer_class = serializer.AdminManageBallotBox
    permission_classes = [permissions.IsAuthenticated,custom_permission.IsAdminOrSuperAdmin]
    

    def _check_is_close(self,id):
        "this check if an election is close"
        election = get_object_or_404(self.get_queryset(), pk=id) 
        if election.is_close == True:raise custom_exceptions.CustomError({"error":"This Election is close"})
    

    @action(detail=False,methods=['get'],permission_classes=[permissions.IsAuthenticated])
    def list_of_elections(self,request,pk=None):
        return custom_response.Success_response(msg='Success',data=self.queryset.all().values())

    @action(detail=False,methods=['get'],permission_classes=[permissions.IsAuthenticated])
    def list_of_contestant(self,request,pk=None):
        election_id = self.request.query_params.get("election_id",None)
        if election_id is None:
            raise custom_exceptions.CustomError({"election_id":"Election Not Found"})
        if not self.queryset.filter(id = election_id).exists():
            raise custom_exceptions.CustomError({"err":"Election Not found"})

        clean_data = serializer.ContestantCleaner(instance=models.Contestant.objects.filter(ballotbox__id =election_id),many=True)
        return custom_response.Success_response(msg='Success',data=clean_data.data)
        

    @action(detail=False,methods=['post'],serializer_class=serializer.AdminManageContest,
    parser_classes = (custom_parsers.NestedMultipartParser,FormParser,)
    )
    def create_contestant(self,request,pk=None):
        serialzied_data = self.serializer_class(data=request.data)
        serialzied_data.is_valid(raise_exception=True)
        self._check_is_close(request.data.get('ballotbox'))
        data = serialzied_data.save()
        return custom_response.Success_response(msg='Success',data=[{
                    "member": data.member.id,
                    "ballotbox": data.ballotbox.id,
                    "amount_vote": data.amount_vote,
                    "youtubeVidLink": data.youtubeVidLink,
                }],status_code=status.HTTP_201_CREATED)

    @action(detail=False,methods=['post'],serializer_class=serializer.MembersVoteSerializer,permission_classes=[permissions.IsAuthenticated,custom_permission.IsMember])
    def vote_for_contestant(self,request,pk=None):
        "memebers can vote for another member"
        if not models.BallotBox.objects.all().filter(id=request.data.get('ballotBoxID')).exists():
            raise custom_exceptions.CustomError({"ballotBoxID":"Election Does not exist"})
        if not models.Contestant.objects.all().filter(id=request.data.get('contestantID')).exists():
            raise custom_exceptions.CustomError({"contestantID":"Contestant Does not exist"})
        # the object of the person we want to vte
        contestant = models.Contestant.objects.get(id=request.data.get('contestantID'))
        serialzied_data = self.serializer_class(instance=contestant,data=request.data,context={"member":user_models.Memeber.objects.get(user=request.user)})
        serialzied_data.is_valid(raise_exception=True)
        self._check_is_close(request.data.get('ballotBoxID'))
        data = serialzied_data.save()
        clean_data = serializer.ContestantCleaner(instance=data,many=True)
        return custom_response.Success_response(msg='Vote Successfull',data=clean_data.data,status_code=status.HTTP_201_CREATED)


