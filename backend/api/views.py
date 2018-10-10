from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import api.serializers as serializers
from api.models import Availability, Match, Profile, PsychePreference, Psychograph, Team
from api.util import gen_new_matches
from api.serializers import ProfileSerializer, UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = serializers.AvailabilitySerializer


class PsychePreferenceViewSet(viewsets.ModelViewSet):
    queryset = PsychePreference.objects.all()
    serializer_class = serializers.PsychePreferenceSerializer


class PsychographViewSet(viewsets.ModelViewSet):
    queryset = Psychograph.objects.all()
    serializer_class = serializers.PsychographSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = serializers.MatchSerializer


@api_view(["GET", "POST"])
def calibrate(request):
    if request.method == "POST":
        # store calibration results
        return Response({"message": "Got data", "data": request.data})
    else:
        # retrieve data required for calibration
        psychographs = Psychograph.objects.filter(calibrator=True)
        data = [serializers.PsychographSerializer(ps).data for ps in psychographs]
        return Response({"psychographs": data})


@api_view(["GET"])
def get_new_matches(request, user_id):
    if user_id:
        matches = gen_new_matches(user_id=user_id, num_matches=5)
        return Response({"matches": matches})
    else:
        return Response({"error": "No user id supplied"})

#The view for making and getting profiles

#This view should serve to return specific profiles, or create profiles 
#One view to get, one to post/etc. split it that way. 

@api_view(['GET','POST'])
def profile_list(request):

    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Got data", "data": serializer.data})
        return Response({"error": serializer.errors})

@api_view(['GET','PUT','DELETE'])
def ProfileDetail(request,pk):

    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found with given UUID"})
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors})

    elif request.method == 'DELETE':
        profile.delete()
        return Response({"message": "profile deleted"})

#Repeat above process for user view.
#Note that, in order to post a new user, you need to provide a username. 

@api_view(['GET','POST'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Got data", "data": serializer.data})
        return Response({"error": serializer.errors})

@api_view(['GET','PUT','DELETE'])
def UserDetail(request,id):

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"error": "User not found with given username"})
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors})

    elif request.method == 'DELETE':
        user.delete()
        return Response({"message": "user deleted"})
