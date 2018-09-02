from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import api.serializers as serializers
from api.models import Profile, Team, Availability, PsychePreference, Psychograph
from api.util import gen_matches

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
def get_matches(request, user_id):
    if user_id:
        matches = gen_matches(user_id=user_id, num_matches=5)
        return Response({'matches': matches})
    else:
        return Response({'error': 'No user id supplied'})
