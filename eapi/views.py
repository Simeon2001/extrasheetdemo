from django.shortcuts import render
from rest_framework import status
# Create your views here.
#from django.contrib.auth import get_user_model
from rest_framework import viewsets # new
from extrasheet.models import Profile,Club
#from .permissions import IsAuthorOrReadOnly
from .serializers import ProfileSerializer,ClubSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ProfileViewSet(viewsets.ModelViewSet): # new
#permission_classes = (IsAuthorOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    
class ClubViewSet(viewsets.ModelViewSet): # new
    pass
#permission_classes = (IsAuthorOrReadOnly,)
"""    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    @action(detail=False)
    def create_club(self,request):
        create_clu = Club.objects.all()
        serialize = (create_clu,many=True,)
        return Response(serialize.data)
        
    @action(detail=False)
    def club(self,request):
        clu = Club.objects.all()
        serialize = (clu,many=True,)
        return Response(serialize.data)"""        
    
    
