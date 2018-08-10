from django.contrib.auth.models import User
from rest_framework import viewsets
import api.serializers as serializers
from api.models import (
    Profile,
    Team,
    Availability,
    PsychePreference
)

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
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