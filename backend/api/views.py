from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import api.serializers as serializers
from api.models import (
    Availability,
    Endorsement,
    Endorsements,
    LaddrMatch,
    Profile,
    PsychePreference,
    Psychograph,
    Team,
)

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


class LaddrMatchViewSet(viewsets.ModelViewSet):
    queryset = LaddrMatch.objects.all()
    serializer_class = serializers.LaddrMatchSerializer


class EndorsementViewSet(viewsets.ModelViewSet):
    queryset = Endorsement.objects.all()
    serializer_class = serializers.EndorsementSerializer


class EndorsementsViewSet(viewsets.ModelViewSet):
    queryset = Endorsements.objects.all().order_by('endorsee')
    serializer_class = serializers.EndorsementsSerializer


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
def loading_taglines(request):
    return Response([
        "Ganking Mid",
        "Floating Mana",
        "Clearing Wraiths",
        "Stealing Baron",
        "Raising Dongers",
    ])
